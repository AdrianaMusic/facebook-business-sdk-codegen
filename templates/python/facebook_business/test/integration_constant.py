# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# This file stores the information needed to perform integration testing
# on the Python Ads SDK.

class FieldName:
    ACCOUNT_ID = 'account_id'
    ADLABELS = 'adlabels'
    BID_STRATEGY = 'bid_strategy'
    BOOSTED_OBJECT_ID = 'boosted_object_id'
    BRAND_LIFT_STUDIES = 'brand_lift_studies'
    BUDGET_REBALANCE_FLAG = 'budget_rebalance_flag'
    BUDGET_REMAINING = 'budget_remaining'
    BUYING_TYPE = 'buying_type'
    CAN_CREATE_BRAND_LIFT_STUDY = 'can_create_brand_lift_study'
    CAN_USE_SPEND_CAP = 'can_use_spend_cap'
    CONFIGURED_STATUS = 'configured_status'
    CREATED_TIME = 'created_time'
    DAILY_BUDGET = 'daily_budget'
    EFFECTIVE_STATUS = 'effective_status'
    EXECUTION_OPTIONS = 'execution_options'
    ID = 'id'
    ISSUES_INFO = 'issues_info'
    ITERATIVE_SPLIT_TEST_CONFIGS = 'iterative_split_test_configs'
    LAST_BUDGET_TOGGLING_TIME = 'last_budget_toggling_time'
    LIFETIME_BUDGET = 'lifetime_budget'
    NAME = 'name'
    OBJECTIVE = 'objective'
    RECOMMENDATIONS = 'recommendations'
    PACING_TYPE = 'pacing_type'
    PROMOTED_OBJECT = 'promoted_object'
    SOURCE_CAMPAIGN_ID = 'source_campaign_id'
    SPECIAL_AD_CATEGORY = 'special_ad_category'
    SPEND_CAP = 'spend_cap'
    STATUS = 'status'
    TOPLINE_ID = 'topline_id'
    START_TIME = 'start_time'
    STOP_TIME = 'stop_time'
    UPDATED_TIME = 'updated_time'
    UPSTREAM_EVENTS = 'upstream_events'

class TestValue:
    ACCESS_TOKEN = 'accesstoken'
    ACCOUNT_ID = 'act_123'
    AD_LABEL = '{"name": "test_label"}'
    ADSET_ID = '12345'
    ADSET_SCHEDULE = '{"pacing_type": "standard"}'
    APP_ID = '1234567'
    APP_SECRET = 'appsecret'
    APP_URL = 'http://test.com'
    ASSET_FEED_ID = '123'
    BID_ADJUSTMENTS = '{"user_groups": "test_group"}'
    BID_AMOUNT = '30000'
    BID_STRATEGY = 'LOWEST_COST_WITHOUT_CAP'
    BILLING_EVENT = 'IMPRESSIONS'
    BOOSTED_OBJECT_ID = '12345678'
    BRAND_LIFT_STUDIES = (
        '{'
        '"id": "cell_id",'
        '"name":"Group A",'
        '"treatment_percentage": "50",'
        '"adsets": {"id" : "adset_id"}'
        '}'
    )
    BUDGET_REBALANCE_FLAG = 'false'
    BUDGET_REMAINING = '150'
    BUSINESS_ID = '111111'
    BUYING_TYPE = 'AUCTION'
    CAMPAIGN_ID = '1234321'
    CAN_CREATE_BRAND_LIFT_STUDY = 'true'
    CAN_USE_SPEND_CAP = 'true'
    CONFIGURED_STATUS = 'PAUSED'
    CREATED_TIME = '3728193'
    DAILY_BUDGET = '200'
    DAILY_MIN_SPEND_TARGET = '50'
    DATE_FORMAT = 'U'
    EFFECTIVE_STATUS = 'PAUSED'
    EXECUTION_OPTIONS = 'include_recommendations'
    INSTAGRAM_ACTOR_ID = '12321'
    ISSUES_INFO = (
        '{'
        '"level": "AD",'
        '"error_code": "1815869",'
        '"error_summary": "Ad post is not available"'
        '}'
    )
    ITERATIVE_SPLIT_TEST_CONFIGS = '{"name": "test_config"}'
    LAST_BUDGET_TOGGLING_TIME = '3892193'
    LIFETIME_BUDGET = '10000'
    NAME = 'test_name'
    OBJECTIVE = 'LINK_CLICKS'
    OPTIMIZATION_GOAL = 'LINK_CLICKS'
    PACING_TYPE = 'standard'
    PAGE_ID = '13531'
    PROMOTED_OBJECT = '{"page_id": "13531"}'
    RECOMMENDATIONS = '{"code": "1772120"}'
    REVIEW_FEEDBACK = 'test review'
    SECONDARY_BUSINESS_ID = '2222222'
    SECONDARY_ACCOUNT_ID = 'act_456'
    SECONDARY_PAGE_ID = '24642'
    SPECIAL_AD_CATEGORY = 'EMPLOYMENT'
    SPEND_CAP = '922337203685478'
    START_TIME = '3728232'
    STATUS = 'PAUSED'
    STOP_TIME = '3872293'
    TOPLINE_ID = '32123'
    TUNE_FOR_CATEGORY = 'CREDIT'
    UPDATED_TIME = '3728132'
    UPSTREAM_EVENTS = '{"name": "event_1", "event_id": "12121"}'
