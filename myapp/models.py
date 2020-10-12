from django.db import models
from mdeditor.fields import MDTextField

# 自定义管理器
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

# 书籍
class Book(models.Model):
    name = models.CharField(max_length=30, verbose_name="书名")

    def all_article_count(self):
        return self.article.filter(status="published").count()
    
    class Meta:
        verbose_name = "书籍"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 文章
class Article(models.Model):
    objects = models.Manager()
    published = PublishedManager()
    STATUS_CHOICE = (("draft", "草稿"), ("published", "发布中"))
    title = models.CharField(max_length=30, verbose_name="标题", unique=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="article", verbose_name="书名")
    # content = models.TextField(verbose_name="正文")
    content = MDTextField(verbose_name="正文")
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default="draft", verbose_name="文章状态")
    priority = models.IntegerField(default=0, verbose_name="优先级")
    look = models.IntegerField(default=0, verbose_name="浏览量")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="发布日期")

    def book_name(self):
        return self.book.name

    def get_absolute_url(self):
        return "/article/{}".format(self.id)

    class Meta:
        ordering = ('priority',)
        verbose_name = "文章列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

# 友链
class Links(models.Model):
    title = models.CharField(max_length=30, verbose_name="标题")
    url = models.URLField(verbose_name="url链接")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "友链"
        verbose_name_plural = verbose_name

class Comment(models.Model):
    username = models.CharField(max_length=20, verbose_name="用户名")
    QQ = models.CharField(max_length=2000, verbose_name="QQ")
    content = models.TextField(verbose_name="评论内容")
    ip = models.CharField(max_length=255, verbose_name="客户端ip地址")
    blog = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comment", verbose_name="博客")
    is_show = models.BooleanField(default=False, verbose_name="是否显示出来")
    reply = models.TextField(default="谢谢你支持我，评论我的博客！", verbose_name="作者的回复")

    def __str__(self):
        return "<comment:{}>".format(self.username)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name