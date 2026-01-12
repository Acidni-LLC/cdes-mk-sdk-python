"""
CDES-MK: Cannabis Data Exchange Standard - Marketing Extension

Marketing and demand generation SDK for cannabis industry.
Includes loyalty programs, campaigns, deals, and analytics integrations.

Extensions:
- AlpineIQ, Springbig, Fyllo, Surfside, Headset integrations
- Customer profiles and segmentation
- Campaign management
- Deal/promotion engine
- Attribution and analytics
"""

__version__ = "0.1.0"
__author__ = "Acidni LLC"

from cdes_mk.models import (
    # Enums
    CustomerStatus,
    ConsentType,
    ConsentStatus,
    SegmentType,
    PointsTransactionType,
    RewardType,
    DealType,
    CampaignStatus,
    CampaignType,
    MessageStatus,
    AttributionModel,
    # Customer Models
    ConsentRecord,
    CustomerPreferences,
    CustomerProfile,
    Customer,
    CustomerSegment,
    # Loyalty Models
    LoyaltyTier,
    LoyaltyProgram,
    LoyaltyMember,
    PointsTransaction,
    Reward,
    RewardRedemption,
    # Deal Models
    DealCondition,
    Deal,
    DealRedemption,
    # Campaign Models
    CampaignAudience,
    CampaignContent,
    CampaignSchedule,
    Campaign,
    CampaignMessage,
    # Analytics Models
    MarketingEvent,
    Attribution,
)

__all__ = [
    "__version__",
    # Enums
    "CustomerStatus",
    "ConsentType", 
    "ConsentStatus",
    "SegmentType",
    "PointsTransactionType",
    "RewardType",
    "DealType",
    "CampaignStatus",
    "CampaignType",
    "MessageStatus",
    "AttributionModel",
    # Customer Models
    "ConsentRecord",
    "CustomerPreferences",
    "CustomerProfile",
    "Customer",
    "CustomerSegment",
    # Loyalty Models
    "LoyaltyTier",
    "LoyaltyProgram",
    "LoyaltyMember",
    "PointsTransaction",
    "Reward",
    "RewardRedemption",
    # Deal Models
    "DealCondition",
    "Deal",
    "DealRedemption",
    # Campaign Models
    "CampaignAudience",
    "CampaignContent",
    "CampaignSchedule",
    "Campaign",
    "CampaignMessage",
    # Analytics Models
    "MarketingEvent",
    "Attribution",
]
