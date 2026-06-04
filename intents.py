

intent_actions = {
    
    # 1. BANKING DOMAIN (15 Intents)
    "banking": {
        "transfer": ["initiate_transfer", "send_money"],
        "balance": ["check_balance", "fetch_account_summary"],
        "transactions": ["view_transaction_history", "filter_transactions"],
        "freeze_account": ["lock_card", "suspend_account_access"],
        "pay_bill": ["schedule_bill_payment", "pay_utility"],
        "bill_balance": ["view_due_amount", "check_next_bill_date"],
        "bill_due": ["get_bill_deadline", "check_overdue_status"],
        "interest_rate": ["get_current_rates", "savings_yield_info"],
        "routing": ["get_routing_number", "ach_routing_info"],
        "account_notification": ["manage_alerts", "toggle_sms_notifications"],
        "pin_change": ["reset_atm_pin", "update_security_pin"],
        "report_fraud": ["flag_transaction", "alert_fraud_department"],
        "order_checks": ["request_checkbook", "track_checkbook_delivery"],
        "direct_deposit": ["setup_direct_deposit", "view_deposit_form"],
        "min_balance": ["check_minimum_balance_requirement", "avoid_fees_info"]
    },

    # 2. CREDIT CARDS DOMAIN (15 Intents)
    "credit_cards": {
        "credit_limit": ["check_credit_limit", "available_credit"],
        "credit_limit_change": ["request_limit_increase", "lower_credit_limit"],
        "credit_score": ["fetch_credit_score", "credit_report_update"],
        "card_declined": ["troubleshoot_declined_card", "check_card_blocks"],
        "rewards_balance": ["view_points", "cashback_balance"],
        "redeem_rewards": ["spend_points", "claim_cashback"],
        "application_status": ["track_card_application", "check_approval_status"],
        "damaged_card": ["request_replacement_card", "report_broken_card"],
        "lost_card": ["cancel_lost_card", "expedite_new_card"],
        "expiration_date": ["get_card_expiry", "renew_expired_card"],
        "international_fees": ["check_foreign_transaction_fees", "travel_rates"],
        "travel_notification": ["add_travel_itinerary", "prevent_international_blocks"],
        "apr": ["view_interest_rate", "check_promotional_apr"],
        "replacement_card_duration": ["track_shipping_eta", "card_delivery_status"],
        "new_card": ["activate_new_card", "browse_available_cards"]
    },

    # 3. TRAVEL DOMAIN (15 Intents)
    "travel": {
        "flight_status": ["check_flight_delay", "track_live_flight"],
        "book_flight": ["search_flights", "purchase_tickets"],
        "book_hotel": ["search_hotels", "reserve_room"],
        "car_rental": ["find_rental_cars", "book_vehicle"],
        "vacation_days": ["check_pto_balance", "request_time_off"],
        "vacation_days_remaining": ["get_remaining_leave", "unused_vacation_hours"],
        "translate": ["open_translator", "convert_language"],
        "travel_alert": ["check_travel_advisories", "weather_warnings"],
        "travel_suggestion": ["get_itinerary_recommendations", "top_destinations"],
        "visa": ["check_visa_requirements", "passport_validity_rules"],
        "exchange_rate": ["convert_currency", "live_forex_rates"],
        "vaccines": ["check_required_immunizations", "travel_health_info"],
        "plug_type": ["check_outlet_type", "voltage_requirements"],
        "lost_luggage": ["file_baggage_claim", "track_lost_bags"],
        "timezone": ["get_local_time", "calculate_time_difference"]
    },

    # 4. HOME DOMAIN (15 Intents)
    "home": {
        "shopping_list": ["view_grocery_list", "add_item_to_list"],
        "shopping_list_update": ["remove_item", "clear_shopping_list"],
        "todo_list": ["get_tasks", "create_new_task"],
        "todo_list_update": ["mark_task_completed", "delete_task"],
        "calendar": ["view_agenda", "check_daily_schedule"],
        "calendar_update": ["add_calendar_event", "reschedule_meeting"],
        "reminder": ["set_alarm_reminder", "get_active_reminders"],
        "reminder_update": ["cancel_reminder", "snooze_reminder"],
        "alarm": ["set_wake_up_alarm", "list_active_alarms"],
        "next_holiday": ["check_upcoming_public_holiday", "holiday_calendar"],
        "current_location": ["get_gps_coordinates", "find_my_address"],
        "timer": ["start_countdown", "stopwatch"],
        "weather": ["get_weather_forecast", "check_rain_chance"],
        "definitions": ["lookup_dictionary", "define_word"],
        "spelling": ["verify_word_spelling", "grammar_check"]
    },

    # 5. UTILITY DOMAIN (15 Intents)
    "utility": {
        "calculator": ["evaluate_math_expression", "solve_equation"],
        "date": ["get_current_date", "day_of_the_week"],
        "time": ["get_current_time", "exact_timestamp"],
        "timer_status": ["check_remaining_timer_time", "pause_timer"],
        "share_location": ["send_live_location", "generate_location_link"],
        "find_phone": ["ping_lost_device", "trigger_phone_ring"],
        "text": ["send_sms_message", "draft_text"],
        "make_call": ["initiate_voice_call", "dial_number"],
        "speed_test": ["measure_internet_speed", "ping_test"],
        "bluetooth": ["toggle_bluetooth", "pair_device"],
        "sync_device": ["force_cloud_sync", "update_connected_appliances"],
        "flashlight": ["turn_on_torch", "turn_off_torch"],
        "volume_up": ["increase_audio_level", "max_volume"],
        "volume_down": ["decrease_audio_level", "mute_audio"],
        "brightness": ["adjust_screen_dimming", "night_mode"]
    },

    # 6. KITCHEN & DINING DOMAIN (15 Intents)
    "kitchen_dining": {
        "recipe": ["search_cooking_recipes", "find_ingredients"],
        "ingredients_list": ["check_recipe_necessities", "pantry_inventory"],
        "calories": ["track_nutritional_value", "lookup_calorie_count"],
        "nutritional_info": ["check_macros", "allergen_warnings"],
        "meal_suggestion": ["generate_dinner_ideas", "diet_plan_recommendation"],
        "restaurant_reviews": ["read_yelp_reviews", "check_star_ratings"],
        "restaurant_reservation": ["book_table", "modify_reservation"],
        "find_restaurants": ["locate_nearby_eateries", "open_restaurants_near_me"],
        "restaurant_suggestion": ["recommend_food_spots", "top_rated_diners"],
        "order": ["place_food_delivery_order", "checkout_cart"],
        "order_status": ["track_delivery_driver", "eta_food_arrival"],
        "cancel_order": ["abort_food_delivery", "request_refund"],
        "cook_time": ["get_baking_duration", "preheat_guidelines"],
        "measurement_conversion": ["convert_cups_to_grams", "metric_units"],
        "food_last": ["check_expiration_shelf_life", "spoilage_guidelines"]
    },

    # 7. AUTO & COMMUTE DOMAIN (15 Intents)
    "auto_commute": {
        "traffic": ["check_commute_delays", "live_traffic_map"],
        "directions": ["get_navigation_route", "gps_turn_by_turn"],
        "distance": ["calculate_mileage", "how_far_is_destination"],
        "gas": ["find_cheapest_gas_stations", "fuel_near_me"],
        "gas_type": ["premium_vs_regular", "octane_requirements"],
        "mpg": ["check_fuel_efficiency", "calculate_trip_mpg"],
        "oil_change_when": ["check_maintenance_schedule", "oil_life_percentage"],
        "oil_change_how": ["diy_oil_change_tutorial", "mechanic_instructions"],
        "tire_pressure": ["check_psi_recommendation", "low_tire_warning"],
        "tire_change": ["roadside_assistance", "how_to_swap_flat_tire"],
        "jump_start": ["how_to_use_jumper_cables", "request_battery_boost"],
        "car_warning_light": ["diagnose_dashboard_icon", "check_engine_meaning"],
        "schedule_maintenance": ["book_mechanic_appointment", "car_service"],
        "uber": ["request_rideshare", "check_uber_fare"],
        "toll_by_plate": ["check_toll_fees", "manage_express_pass"]
    },

    # 8. WORK DOMAIN (15 Intents)
    "work": {
        "schedule_meeting": ["invite_attendees", "create_zoom_link"],
        "meeting_schedule": ["list_todays_meetings", "next_conference"],
        "income": ["view_paystub", "salary_details"],
        "taxes": ["download_w2_form", "tax_withholding"],
        "payday": ["check_next_payroll_date", "direct_deposit_arrival"],
        "rollover_401k": ["manage_retirement_funds", "investment_allocation"],
        "insurance": ["view_health_benefits", "dental_vision_coverage"],
        "pto_request": ["submit_time_off_form", "manager_leave_approval"],
        "pto_status": ["track_leave_request_approval", "approved_pto_dates"],
        "w2": ["get_tax_documents", "employer_identification_number"],
        "performance_review": ["read_manager_feedback", "self_evaluation_form"],
        "expense_report": ["submit_receipts", "reimbursement_status"],
        "indirect_post": ["internal_announcements", "company_bulletin"],
        "company_policy": ["search_employee_handbook", "hr_rules"],
        "plug_in": ["it_support_ticket", "hardware_setup"]
    },

    # 9. META DOMAIN (15 Intents)
    "meta": {
        "change_user_name": ["update_profile_name", "set_nickname"],
        "change_ai_name": ["rename_assistant", "custom_wake_word"],
        "cancel": ["abort_current_operation", "stop_process"],
        "user_name": ["retrieve_user_profile_name", "who_am_i"],
        "reset": ["restore_factory_settings", "wipe_session_context"],
        "speak_louder": ["increase_tts_volume", "voice_gain_up"],
        "whisper": ["enable_quiet_mode", "low_voice_output"],
        "repeat": ["replay_last_response", "say_again"],
        "update_system": ["download_latest_firmware", "patch_software"],
        "yes": ["confirm_action", "positive_affirmation"],
        "no": ["deny_action", "negative_response"],
        "maybe": ["ambiguous_response", "request_clarification"],
        "help": ["open_documentation", "list_available_commands"],
        "capabilities": ["what_can_you_do", "features_list"],
        "change_language": ["switch_voice_locale", "set_system_language"]
    },

    # 10. SMALL TALK DOMAIN (15 Intents)
    "small_talk": {
        "greeting": ["respond_hello", "say_good_morning"],
        "goodbye": ["respond_bye", "terminate_session"],
        "thank_you": ["acknowledge_gratitude", "you_are_welcome"],
        "tell_joke": ["fetch_random_joke", "humor_delivery"],
        "fun_fact": ["fetch_trivia_fact", "did_you_know"],
        "how_old_are_you": ["bot_age_response", "system_creation_date"],
        "where_are_you_from": ["bot_origin_story", "cloud_hosting_info"],
        "what_is_your_name": ["state_identity", "introduce_self"],
        "what_are_your_hobbies": ["bot_hobbies_response", "synthetic_interests"],
        "are_you_a_bot": ["confirm_ai_status", "human_vs_machine_response"],
        "who_made_you": ["attribute_creators", "developer_credit"],
        "meaning_of_life": ["philosophical_easter_egg", "42"],
        "weather_chat": ["casual_weather_remark", "nice_day_out_huh"],
        "do_you_love_me": ["sentimental_bot_response", "friendship_affirmation"],
        "talk_to_human": ["escalate_to_live_agent", "transfer_to_support"]
    },

    # 11. OUT OF SCOPE (1 Intent)
    "out_of_scope": {
        "oos": ["trigger_fallback_response", "log_unsupported_utterance"]
    }
}