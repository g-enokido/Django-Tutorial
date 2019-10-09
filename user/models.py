from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator
    username = models.CharField(
        _('username'), max_length=150,
        unique=True, help_text='ユーザー名は英数字150以内で入力してください。',
        validators=[username_validator],
        error_messages={'unique': _("そのユーザー名はすでに使用されています"), },)

    email = models.EmailField(
        _('email address'), blank=True,)

    profile_icon = models.ImageField(
        _('profile icon'), upload_to='profile_icons', null=True, blank=True, )

    self_introduction = models.CharField(
        _('self introduction'), max_length=512, blank=True, )

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
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'users'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
