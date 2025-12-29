from django.core.exceptions import PermissionDenied

class ApenasRecepcionistaMixin:
    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            raise PermissionDenied("Você precisa estar logado.")

        if not hasattr(request.user, 'profissional'):
            raise PermissionDenied("Usuário não possui perfil profissional.")

        if request.user.profissional.tipo != 'recepcionista':
            raise PermissionDenied("Apenas recepcionistas podem acessar esta página.")

        return super().dispatch(request, *args, **kwargs)