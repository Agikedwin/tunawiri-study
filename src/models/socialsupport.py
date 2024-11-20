from datetime import datetime
from pydantic import BaseModel,Field
import uuid


class SocialSupportModel(BaseModel):
        id: object = Field(default_factory=uuid.uuid4, alias='_id')
        user_id: object
        timepoint: str
        #insulted_feelings: str
        #belittled_humiliated: str
        #scare_intimidate: str
        #threw_out_house: str
        #confined_locked: str
        #threatened_hurt: str
        #slapped_thrown: str
        #pushed_dhoved: str
        hit_with_fist: str
        kicked_dragged: str
        #choked_burnt: str
        #threatened_used_weapon: str
        #forced_sexual_Intercourse: str
        #agreed_unwanted_Intercourse: str
        #forced_other_sexual_act: str
        #tried_keep_from_friends: str
        #tried_restrict_family_contact: str
        #insisted_knowing_location: str
        #jealous_angry_with_men: str
        #suspicious_unfaithful: str
        #took_earnings_savings: str
        #refused_money_for_household: str
        #tried_convince_crazy: str
        #blamed_for_violent_behavior: str
        created_at:  datetime = datetime.now()
        comment: str | None = None
        timepoint: str | None = None
