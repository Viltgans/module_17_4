from fastapi import APIRouter, Depends, status, HTTPException
from typing import Annotated
from app.backend.db_depends import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix='/task', tags=['task'])

@router.get('/')
async def all_tasks():
     pass

@router.get('/task_id')
async def task_by_id():
     pass

@router.post('/create')
async def create_task():
     pass

@router.put('/update')
async def update_task():
     pass

@router.delete('/delete')
async def delete_task():
     pass