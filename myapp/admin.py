from django.contrib import admin
from . import models
from django.utils.html import format_html

def make_published(modeladmin, request, queryset):
    queryset.update(status='published')
make_published.short_description = "一键发布"

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    actions = [make_published,]
    list_display = ["title", "book_name", "status", "priority",]
    search_fields = ['title', "content"]
    list_editable = ["priority",]
    
@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(models.Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ['title', 'url',]

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    actions = ["make_show",]
    list_display = ['username', 'QQ', "blog", 'ip', "reply", "is_show", "click_send"]
    autocomplete_fields = ['blog',]
    readonly_fields = ['ip', 'blog', 'username', 'QQ', 'content']
    search_fields = ["username", "cotent", "QQ"]

    def make_show(self, request, queryset):
        queryset.update(is_show=True)
    make_show.short_description = "一键显示"

    # 点击a标签发送邮件
    def click_send(self, obj):
        return format_html("<a href={}send/>发送</a>".format(obj.pk))
    click_send.short_description = "发送邮件"

    def get_urls(self):
        from django.urls import path
        urlpatterns = [
            path("<pk>send/", self.admin_site.admin_view(self.send_mail), name="send_mail"),
        ]
        return urlpatterns + super(CommentAdmin, self).get_urls()

    def send_mail(self, request, pk):
        from django.urls import reverse
        from django.core.mail import send_mail
        from myproject.settings import DEFAULT_FROM_EMAIL
        from django.shortcuts import get_object_or_404, redirect

        one = get_object_or_404(models.Comment, pk=pk)
        email_title = "您的评论被回复啦!"
        url = reverse("article", args=[one.blog.pk])
        email_body = "您在 https://www.catfish1921.com 的标题为《{}》的博客留言已被回复，博主给您留言：{}。该文章链接为https://www.catfish1921.com{}".format(one.blog.title, one.reply, url)
        send_to = one.QQ + "@qq.com"
        send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [send_to], fail_silently=False)
        co_path = "/".join(request.path.split("/")[:-2])
        self.message_user(request, "发送成功！")
        return redirect(co_path)