from .role import urlpatterns as role_patterns
from .utilisateur import urlpatterns as utilisateur_patterns

urlpatterns = role_patterns + utilisateur_patterns
