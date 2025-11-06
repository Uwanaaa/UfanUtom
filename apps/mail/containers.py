from dependency_injector import containers, providers
from .application.services import EmailService
from .infrastructure.repositories import EmailRepository
from .domain.models import EmailSubscription
from .application.usecases import EmailUseCase


class MailContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    email_model = providers.Singleton(EmailSubscription)
    email_repository = providers.Singleton(EmailRepository, model=email_model)
    email_service = providers.Singleton(EmailService, repository=email_repository)
    email_usecase = providers.Singleton(EmailUseCase, service=email_service)
