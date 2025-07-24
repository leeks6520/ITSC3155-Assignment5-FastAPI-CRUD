from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

#new orderdetail
def create(db: Session, detail: schemas.OrderDetailCreate):
    # Create a new instance 
    db_detail = models.OrderDetail(
        order_id=detail.order_id,
        sandwich_id=detail.sandwich_id,
        amount=detail.amount
    )
    # Add newly created OrderDetail object to the database session
    db.add(db_detail)
    # Commit changes to the database
    db.commit()
    # Refresh OrderDetail object to ensure it reflects the current state in the database
    db.refresh(db_detail)
    # Return the newly created OrderDetail object
    return db_detail


def read_all(db: Session):
    # Query and return all order details from the database
    return db.query(models.OrderDetail).all()


def read_one(db: Session, detail_id):
    # Query and return a specific order detail by ID
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id).first()


def update(db: Session, detail_id, detail):
    # Query the database for the specific order detail to update
    db_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    # Extract the update data from the provided 'detail' object
    update_data = detail.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_detail.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated order detail record
    return db_detail.first()


def delete(db: Session, detail_id):
    # Query the database for the specific order detail to delete
    db_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    # Delete the database record without synchronizing the session
    db_detail.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
