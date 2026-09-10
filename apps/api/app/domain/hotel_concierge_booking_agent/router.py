from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.hotel_concierge_booking_agent.schemas import AgenticHotelConciergeBookingAgentSessionCreate, AgenticHotelConciergeBookingAgentSessionResponse
from app.domain.hotel_concierge_booking_agent.service import AgenticHotelConciergeBookingAgentService

router = APIRouter(prefix="/api/v1/hotel_concierge_booking_agent", tags=["Agentic Hotel Concierge Booking Agent Domain"])

@router.post("/sessions", response_model=AgenticHotelConciergeBookingAgentSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticHotelConciergeBookingAgentSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Hotel Concierge Booking Agent.
    """
    return AgenticHotelConciergeBookingAgentService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticHotelConciergeBookingAgentSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticHotelConciergeBookingAgentService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
