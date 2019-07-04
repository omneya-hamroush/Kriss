# from rest_framework.authentication import TokenAuthentication
# from django.utils.translation import ugettext_lazy as _
# from rest_framework import HTTP_HEADER_ENCODING, exceptions
# from profiles_api import models
# from rest_framework.authentication import get_authorization_header
#
# class CustomTokenAuthentication(TokenAuthentication):
#     request = None
#     model = models.Token
#
#     def authenticate(self, request):
#         self.request = request
#         auth = request.query_params.get('Authorization', b'').split()
#
#         if not auth:
#             return None
#
#
#         try:
#
#             token = auth[0].decode()
#         except UnicodeError:
#             msg = _(
#                 'Invalid token header. Token string should not contain invalid characters.')
#             raise exceptions.AuthenticationFailed(msg)
#
#         return self.authenticate_credentials(token)
#
#     def authenticate_credentials(self, key):
#         model = self.get_model()
#         try:
#             token = model.objects.select_related('user').get(key=key)
#         except model.DoesNotExist:
#             raise exceptions.AuthenticationFailed(_('Invalid token.'))
#
#         return (token.user, token)
