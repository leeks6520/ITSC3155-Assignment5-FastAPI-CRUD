from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from .models import models, schemas  # Absolute import
from .dependencies.database import get_db
from typing import Annotated

#new resource, follow the same template as orders.py
def create(db: Session, resource: schemas.ResourceCreate):
    db_resource = models.Resource(**resource.model_dump())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource


def read_all(db: Session):
    return db.query(models.Resource).all()


def read_one(db: Session, resource_id: int):
    resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if resource is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    return resource


def update(db: Session, resource_id: int, resource: schemas.ResourceUpdate):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if db_resource is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")

    for key, value in resource.model_dump(exclude_unset=True).items():
        setattr(db_resource, key, value)

    db.add(db_resource)  # Mark for update
    db.commit()
    db.refresh(db_resource)
    return db_resource


def delete(db: Session, resource_id: int):
    resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if resource is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    db.delete(resource)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
