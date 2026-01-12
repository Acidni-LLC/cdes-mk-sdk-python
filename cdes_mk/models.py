"""CDES-MK Core Models - Marketing and demand generation data models."""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, date
from decimal import Decimal
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

class CustomerStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    PENDING_VERIFICATION = "pending_verification"
    CHURNED = "churned"

class ConsentType(str, Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"
    DIRECT_MAIL = "direct_mail"
    PHONE = "phone"
    ALL = "all"

class ConsentStatus(str, Enum):
    OPTED_IN = "opted_in"
    OPTED_OUT = "opted_out"
    PENDING = "pending"
    NEVER_SET = "never_set"

class SegmentType(str, Enum):
    BEHAVIORAL = "behavioral"
    DEMOGRAPHIC = "demographic"
    PURCHASE_BASED = "purchase_based"
    ENGAGEMENT = "engagement"
    LIFECYCLE = "lifecycle"
    CUSTOM = "custom"

class PointsTransactionType(str, Enum):
    EARNED = "earned"
    REDEEMED = "redeemed"
    ADJUSTED = "adjusted"
    EXPIRED = "expired"
    TRANSFERRED = "transferred"
    BONUS = "bonus"
    REFUND = "refund"

class RewardType(str, Enum):
    DISCOUNT_PERCENTAGE = "discount_percentage"
    DISCOUNT_FIXED = "discount_fixed"
    FREE_PRODUCT = "free_product"
    BOGO = "bogo"
    POINTS_MULTIPLIER = "points_multiplier"
    EXCLUSIVE_ACCESS = "exclusive_access"
    FREE_DELIVERY = "free_delivery"

class DealType(str, Enum):
    PERCENTAGE_OFF = "percentage_off"
    DOLLAR_OFF = "dollar_off"
    BOGO = "bogo"
    BUNDLE = "bundle"
    FLASH_SALE = "flash_sale"
    HAPPY_HOUR = "happy_hour"
    FIRST_TIME = "first_time"
    LOYALTY_EXCLUSIVE = "loyalty_exclusive"
    BIRTHDAY = "birthday"
    VETERAN = "veteran"

class CampaignStatus(str, Enum):
    DRAFT = "draft"
    SCHEDULED = "scheduled"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class CampaignType(str, Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"
    MULTI_CHANNEL = "multi_channel"
    DRIP = "drip"
    AUTOMATED = "automated"
    ONE_TIME = "one_time"

class MessageStatus(str, Enum):
    PENDING = "pending"
    SENT = "sent"
    DELIVERED = "delivered"
    OPENED = "opened"
    CLICKED = "clicked"
    BOUNCED = "bounced"
    FAILED = "failed"

class AttributionModel(str, Enum):
    FIRST_TOUCH = "first_touch"
    LAST_TOUCH = "last_touch"
    LINEAR = "linear"
    TIME_DECAY = "time_decay"
    POSITION_BASED = "position_based"

@dataclass
class ConsentRecord:
    consent_type: ConsentType
    status: ConsentStatus
    granted_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None
    source: Optional[str] = None

@dataclass
class CustomerPreferences:
    preferred_channel: Optional[str] = None
    preferred_time: Optional[str] = None
    preferred_frequency: Optional[str] = None
    preferred_language: str = "en"
    preferred_categories: list[str] = field(default_factory=list)

@dataclass
class CustomerProfile:
    customer_id: UUID
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    medical_card_number: Optional[str] = None
    preferred_dispensary_id: Optional[str] = None
    preferred_terpenes: list[str] = field(default_factory=list)
    preferred_effects: list[str] = field(default_factory=list)
    consumption_method: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class Customer:
    id: UUID = field(default_factory=uuid4)
    external_id: Optional[str] = None
    status: CustomerStatus = CustomerStatus.ACTIVE
    profile: Optional[CustomerProfile] = None
    preferences: CustomerPreferences = field(default_factory=CustomerPreferences)
    consents: list[ConsentRecord] = field(default_factory=list)
    segment_ids: list[str] = field(default_factory=list)
    loyalty_member_id: Optional[str] = None
    lifetime_value: Decimal = Decimal("0.00")
    total_orders: int = 0
    first_purchase_date: Optional[datetime] = None
    last_purchase_date: Optional[datetime] = None
    created_at: datetime = field(default_factory=datetime.utcnow)

    def has_consent(self, consent_type: ConsentType) -> bool:
        for consent in self.consents:
            if consent.consent_type in (consent_type, ConsentType.ALL):
                return consent.status == ConsentStatus.OPTED_IN
        return False

@dataclass
class CustomerSegment:
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    description: Optional[str] = None
    segment_type: SegmentType = SegmentType.CUSTOM
    criteria: dict = field(default_factory=dict)
    customer_count: int = 0
    is_dynamic: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class LoyaltyTier:
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    level: int = 0
    points_required: int = 0
    points_multiplier: Decimal = Decimal("1.0")
    benefits: list[str] = field(default_factory=list)

@dataclass
class LoyaltyProgram:
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    points_name: str = "points"
    points_per_dollar: Decimal = Decimal("1.0")
    points_expiry_days: Optional[int] = None
    tiers: list[LoyaltyTier] = field(default_factory=list)
    enrollment_bonus: int = 0
    birthday_bonus: int = 0
    is_active: bool = True

@dataclass
class LoyaltyMember:
    id: UUID = field(default_factory=uuid4)
    customer_id: UUID = field(default_factory=uuid4)
    program_id: UUID = field(default_factory=uuid4)
    member_number: Optional[str] = None
    current_tier_id: Optional[UUID] = None
    points_balance: int = 0
    lifetime_points: int = 0
    enrolled_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class PointsTransaction:
    id: UUID = field(default_factory=uuid4)
    member_id: UUID = field(default_factory=uuid4)
    transaction_type: PointsTransactionType = PointsTransactionType.EARNED
    points: int = 0
    balance_after: int = 0
    description: Optional[str] = None
    reference_id: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class Reward:
    id: UUID = field(default_factory=uuid4)
    program_id: UUID = field(default_factory=uuid4)
    name: str = ""
    reward_type: RewardType = RewardType.DISCOUNT_PERCENTAGE
    points_cost: int = 0
    value: Decimal = Decimal("0.00")
    is_active: bool = True
    valid_until: Optional[datetime] = None

@dataclass
class RewardRedemption:
    id: UUID = field(default_factory=uuid4)
    reward_id: UUID = field(default_factory=uuid4)
    member_id: UUID = field(default_factory=uuid4)
    points_spent: int = 0
    order_id: Optional[str] = None
    status: str = "pending"
    redeemed_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class DealCondition:
    min_purchase: Optional[Decimal] = None
    min_quantity: Optional[int] = None
    required_products: list[str] = field(default_factory=list)
    required_categories: list[str] = field(default_factory=list)
    customer_segments: list[str] = field(default_factory=list)
    first_time_only: bool = False
    max_uses_per_customer: Optional[int] = None

@dataclass
class Deal:
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    description: Optional[str] = None
    deal_type: DealType = DealType.PERCENTAGE_OFF
    value: Decimal = Decimal("0.00")
    promo_code: Optional[str] = None
    conditions: DealCondition = field(default_factory=DealCondition)
    stackable: bool = False
    is_active: bool = True
    valid_from: datetime = field(default_factory=datetime.utcnow)
    valid_until: Optional[datetime] = None

@dataclass
class DealRedemption:
    id: UUID = field(default_factory=uuid4)
    deal_id: UUID = field(default_factory=uuid4)
    customer_id: UUID = field(default_factory=uuid4)
    order_id: str = ""
    discount_applied: Decimal = Decimal("0.00")
    redeemed_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class CampaignAudience:
    segment_ids: list[UUID] = field(default_factory=list)
    include_all_customers: bool = False
    exclude_segment_ids: list[UUID] = field(default_factory=list)
    estimated_size: int = 0

@dataclass
class CampaignContent:
    subject: Optional[str] = None
    body_html: Optional[str] = None
    body_text: Optional[str] = None
    sms_text: Optional[str] = None
    image_url: Optional[str] = None
    cta_text: Optional[str] = None
    cta_url: Optional[str] = None

@dataclass
class CampaignSchedule:
    send_at: Optional[datetime] = None
    send_in_recipient_timezone: bool = False
    recurring: bool = False

@dataclass
class Campaign:
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    campaign_type: CampaignType = CampaignType.ONE_TIME
    status: CampaignStatus = CampaignStatus.DRAFT
    audience: CampaignAudience = field(default_factory=CampaignAudience)
    content: CampaignContent = field(default_factory=CampaignContent)
    schedule: CampaignSchedule = field(default_factory=CampaignSchedule)
    deal_ids: list[UUID] = field(default_factory=list)
    total_sent: int = 0
    total_opened: int = 0
    total_clicked: int = 0
    total_converted: int = 0
    total_revenue: Decimal = Decimal("0.00")
    created_at: datetime = field(default_factory=datetime.utcnow)

    @property
    def open_rate(self) -> float:
        return (self.total_opened / self.total_sent * 100) if self.total_sent else 0.0

    @property
    def click_rate(self) -> float:
        return (self.total_clicked / self.total_sent * 100) if self.total_sent else 0.0

@dataclass
class CampaignMessage:
    id: UUID = field(default_factory=uuid4)
    campaign_id: UUID = field(default_factory=uuid4)
    customer_id: UUID = field(default_factory=uuid4)
    channel: str = ""
    status: MessageStatus = MessageStatus.PENDING
    recipient: str = ""
    sent_at: Optional[datetime] = None
    opened_at: Optional[datetime] = None
    clicked_at: Optional[datetime] = None

@dataclass
class MarketingEvent:
    id: UUID = field(default_factory=uuid4)
    event_type: str = ""
    customer_id: Optional[UUID] = None
    campaign_id: Optional[UUID] = None
    deal_id: Optional[UUID] = None
    properties: dict = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.utcnow)

@dataclass
class Attribution:
    id: UUID = field(default_factory=uuid4)
    order_id: str = ""
    customer_id: UUID = field(default_factory=uuid4)
    order_total: Decimal = Decimal("0.00")
    attribution_model: AttributionModel = AttributionModel.LAST_TOUCH
    touchpoints: list[dict] = field(default_factory=list)
    attributed_campaign_id: Optional[UUID] = None
    attributed_channel: Optional[str] = None
    days_to_conversion: int = 0
    created_at: datetime = field(default_factory=datetime.utcnow)

__all__ = [
    "CustomerStatus", "ConsentType", "ConsentStatus", "SegmentType",
    "PointsTransactionType", "RewardType", "DealType", "CampaignStatus",
    "CampaignType", "MessageStatus", "AttributionModel",
    "ConsentRecord", "CustomerPreferences", "CustomerProfile", "Customer", "CustomerSegment",
    "LoyaltyTier", "LoyaltyProgram", "LoyaltyMember", "PointsTransaction", "Reward", "RewardRedemption",
    "DealCondition", "Deal", "DealRedemption",
    "CampaignAudience", "CampaignContent", "CampaignSchedule", "Campaign", "CampaignMessage",
    "MarketingEvent", "Attribution",
]
