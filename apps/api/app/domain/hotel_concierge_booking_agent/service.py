from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.hotel_concierge_booking_agent.models import AgenticHotelConciergeBookingAgentSession, AgenticHotelConciergeBookingAgentItem
from app.domain.hotel_concierge_booking_agent.schemas import AgenticHotelConciergeBookingAgentSessionCreate, AgenticHotelConciergeBookingAgentItemCreate

class AgenticHotelConciergeBookingAgentService:
    @staticmethod
    def create_session(db: Session, data: AgenticHotelConciergeBookingAgentSessionCreate) -> AgenticHotelConciergeBookingAgentSession:
        db_obj = AgenticHotelConciergeBookingAgentSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticHotelConciergeBookingAgentSession:
        return db.query(AgenticHotelConciergeBookingAgentSession).filter(AgenticHotelConciergeBookingAgentSession.id == session_id).first()
