from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from stdimage import StdImageField
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator
    username = models.CharField(
        _('username'), max_length=150,
        unique=True, help_text='ユーザー名は英数字150以内で入力してください。',
        validators=[username_validator],
        error_messages={'unique': _("そのユーザー名はすでに使用されています"), },)

    email = models.EmailField(
        _('email address'), unique=True,)

    profile_icon = StdImageField(
        verbose_name='アイコン', upload_to='profile_icons/', null=True, blank=True, variations={
            'large': (600, 400),
            'thumbnail': (100, 100, True),
            'medium': (300, 200),
        })

    self_introduction = models.CharField(
        verbose_name='自己紹介', max_length=512, blank=True, )

    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False, help_text='管理者権限を指定します。', )
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text='管理者がこのユーザーをログインできるかを管理します。アカウントを削除する際には、こちらをFlaseにします。',
                                    )
    date_joined = models.DateTimeField(
        _('date joined'), default=timezone.now, )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'users'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Blog(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog_name = models.CharField(max_length=200, verbose_name='ブログタイトル')
    blog_detail = models.TextField(null=True, blank=True, verbose_name='ブログ詳細')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.blog_name
