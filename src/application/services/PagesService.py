from infrastructure.repositories import DjangoPageRepository

def getAllPages():
    repo = DjangoPageRepository()
    return repo.all()
