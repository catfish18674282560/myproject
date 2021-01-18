from django.db import models

class Words(models.Model):
    word = models.CharField(max_length=50, verbose_name="单词")
    hans = models.CharField(max_length=50, verbose_name="中文意思")
    is_recite = models.BooleanField(default=True, verbose_name="是否需要检测背诵")

    def __str__(self):
        return "<单词：{}>".format(self.word)

    class Meta:
        verbose_name = "单词库"
        verbose_name_plural = verbose_name