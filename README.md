# CDES-MK: Cannabis Data Exchange Standard - Marketing Extension

Marketing and demand generation SDK for the cannabis industry. Part of the [CDES](https://cdes.dev) ecosystem.

## Features

- **Customer Profiles** - Unified customer data with consent management
- **Loyalty Programs** - Points, tiers, rewards, and redemptions
- **Campaigns** - Email, SMS, push notification campaign management
- **Deals & Promotions** - Discount engine with complex conditions
- **Analytics** - Marketing attribution and performance tracking

## Platform Integrations

| Platform | Status | Description |
|----------|--------|-------------|
| AlpineIQ |  Ready | Largest cannabis loyalty platform |
| Springbig |  Coming | SMS marketing and loyalty |
| Headset |  Ready | Market intelligence and analytics |
| Fyllo |  Coming | Programmatic cannabis advertising |
| Surfside |  Coming | CDP and audience data |

## Installation

```bash
pip install cdes-mk
```

## Quick Start

```python
from cdes_mk import Customer, LoyaltyProgram, Campaign, Deal

# Create a customer
customer = Customer(
    external_id="POS-12345",
    profile=CustomerProfile(
        first_name="Jane",
        email="jane@example.com",
        preferred_terpenes=["limonene", "myrcene"]
    )
)

# Create a deal
deal = Deal(
    name="First Time Patient",
    deal_type=DealType.PERCENTAGE_OFF,
    value=Decimal("20.00"),
    conditions=DealCondition(first_time_only=True)
)
```

## Documentation

- [Full Documentation](https://cdes.dev/docs/marketing)
- [API Reference](https://cdes.dev/api/cdes-mk)
- [Integration Guides](https://cdes.dev/guides/marketing)

## License

MIT License - see [LICENSE](LICENSE) for details.

## Part of CDES

This SDK is part of the Cannabis Data Exchange Standard ecosystem:

- **CDES** (Core) - Strains, batches, terpenes, cannabinoids
- **CDES-M** - Medical/healthcare (FHIR, HL7)
- **CDES-C** - Commerce (GS1, EDI, e-commerce)
- **CDES-MK** - Marketing (this SDK)
- **CDES-FS** - Food Service (recipes, dosing)

Learn more at [cdes.dev](https://cdes.dev)
