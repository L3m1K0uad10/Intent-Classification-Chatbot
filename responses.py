

intent_responses = {

    # 1. BANKING DOMAIN
    "banking": {
        "transfer": [
            "Sure thing! Who would you like to transfer funds to?",
            "I can help with that. Please enter the recipient's details and the amount to send.",
            "Transfer portal initialized. Let's get that money moved safely."
        ],
        "balance": [
            "Let me check that secure ledger for you. One moment...",
            "Your current available balance across checking and savings is updating now.",
            "Sure, fetching your latest account balances right away."
        ],
        "transactions": [
            "Here is a summary of your recent transactions over the last 30 days.",
            "Pulling up your statement history. Let me know if you are looking for a specific charge.",
            "Loading your recent financial ledger details now."
        ],
        "freeze_account": [
            "🚨 Security alert initiated. I am locking down your account card access immediately.",
            "Card locked successfully. No further charges will go through until you unlock it.",
            "I've suspended access to this card. Let's get you in touch with our security team."
        ],
        "pay_bill": [
            "Which scheduled bill would you like to process today?",
            "Let's settle up. Ready to route your payment details securely.",
            "Bill payment processing dashboard is open."
        ],
        "bill_balance": [
            "Checking outstanding invoices... looks like you have a summary ready.",
            "Your total due across connected utilities is loading now.",
            "Let's see what statements are currently outstanding."
        ],
        "bill_due": [
            "Your next payment cycle deadline is fast approaching. Here are the dates:",
            "Checking upcoming deadlines... don't worry, you still have time.",
            "Let me grab those critical bill milestones for you."
        ],
        "interest_rate": [
            "Our latest high-yield interest tiers and standard APR calculations are ready.",
            "Checking current market APY yields for your account type...",
            "Here are the active yield breakdowns for your savings accounts."
        ],
        "routing": [
            "Your electronic ACH routing transit number is displayed below.",
            "Here is the 9-digit direct deposit and wire routing code.",
            "Found it! Use this specific routing number for standard bank wires."
        ],
        "account_notification": [
            "You can manage SMS alerts, email summaries, and push alerts right here.",
            "Opening your alert profile setup. Let's dial in those updates.",
            "Would you like to turn real-time transaction notifications on or off?"
        ],
        "pin_change": [
            "Security verification approved. Please input your new 4-digit ATM PIN.",
            "Let's update that access PIN. Make sure it's not something easily guessed!",
            "Redirecting to our secure PIN configuration screen."
        ],
        "report_fraud": [
            "🚨 Escalating immediately to Fraud Prevention. Which transaction looks unauthorized?",
            "Let's flag this suspicious activity right away. We've got your back.",
            "Initiating a formal dispute claim. Locking down related access parameters now."
        ],
        "order_checks": [
            "Standard checkbooks come with 100 pages. Confirm your mailing address to ship?",
            "Processing checkbook supply request. Would you like standard or express shipping?",
            "Let's order a fresh book of physical checks for your account."
        ],
        "direct_deposit": [
            "Here is your pre-filled direct deposit authorization document for HR.",
            "Generating your official routing and account slip to configure your payroll.",
            "Let's get your salary routed straight here. Here is your digital form."
        ],
        "min_balance": [
            "To completely waive monthly service fees, keep your daily balance above our threshold.",
            "Checking account minimum rules. Here is how to keep your account completely fee-free:",
            "Here are the baseline minimum values required for this account tier."
        ]
    },

    # 2. CREDIT CARDS DOMAIN
    "credit_cards": {
        "credit_limit": [
            "Your maximum credit allowance and current available room are listed below.",
            "Let's verify how much spending power you have remaining on this cycle.",
            "Pulling up your revolving credit threshold status."
        ],
        "credit_limit_change": [
            "Processing your request for an adjustment. Checking automatic evaluation factors...",
            "Would you like to request a higher spending limit, or lower your maximum threshold?",
            "Let's review if your profile qualifies for an expanded credit line."
        ],
        "credit_score": [
            "Pulling your soft credit check bureau update. Good news, this won't hurt your score!",
            "Your latest credit file summary indicates a strong score posture.",
            "Here is your monthly updated credit health dashboard index."
        ],
        "card_declined": [
            "Let's figure out what went wrong. Checking block triggers, limits, or fraud filters...",
            "Found the issue behind the declined merchant attempt. Here is the clear reason:",
            "Let me look up why your card transaction was bounced back by the processor."
        ],
        "rewards_balance": [
            "You've been racking up points! Here is your loyalty rewards treasure chest:",
            "Loading your total accumulated cashback and point multipliers.",
            "Check out your accrued rewards point balance below!"
        ],
        "redeem_rewards": [
            "Excellent choice. Would you like to apply points as a statement credit or a gift card?",
            "Let's cash those hard-earned rewards points in. What are we buying?",
            "Opening the rewards redemption store for your available balance."
        ],
        "application_status": [
            "Checking underwriting status... your application review is updating.",
            "Let's see where your new card file sits in our automated review pipeline.",
            "Good news! Your pending card application tracking tracker is loading."
        ],
        "damaged_card": [
            "Mangled strip or chipped finish? Let's deactivate the physical token and send a replacement.",
            "No problem, accidents happen. I'll order a duplicate card to be pressed for you.",
            "Let's get a pristine card ordered. The old one will remain active until the new one arrives."
        ],
        "lost_card": [
            "Oh no! Let's completely freeze that specific token instantly so no one else uses it.",
            "Reporting card missing. I've terminated the old number and queued up a new secure token.",
            "Instant lock applied. Let's review final charges to confirm they were actually yours."
        ],
        "expiration_date": [
            "The active card on file concludes its service validation period on the date below.",
            "Checking the plastic expiration matrix... you're good for a while longer!",
            "Here is the valid-thru date printed on the reverse side of your card."
        ],
        "international_fees": [
            "Great news: this premium card tier carries a 0% foreign transaction fee structural rate!",
            "Checking global roaming charges... here are the conversion overhead fees for this card:",
            "Here is the full breakdown of foreign transaction fees before you cross borders."
        ],
        "travel_notification": [
            "Where are you heading? Let's log your itinerary so our security system doesn't block you.",
            "Adding travel flags to your account file. Have a safe and amazing journey!",
            "Configuring holiday location flags so your card works seamlessly abroad."
        ],
        "apr": [
            "Your annual percentage rate calculation for interest cycles is broken down here:",
            "Checking purchase APR vs. cash advance interest penalties...",
            "Here are the underlying interest schedules applied to carried balances."
        ],
        "replacement_card_duration": [
            "Your newly minted card is currently with the courier. Tracking ETA details below:",
            "Standard delivery takes 3-5 business days. Let's look up the express status.",
            "Shipping tracking updated: your replacement card is arriving soon."
        ],
        "new_card": [
            "Welcome! Let's get that shiny new plastic activated and ready to spend.",
            "Ready to turn on your card? Input the 3-digit CVV authorization security number.",
            "Let's activate your fresh digital and physical credit cards right now."
        ]
    },

    # 3. TRAVEL DOMAIN
    "travel": {
        "flight_status": [
            "Fetching real-time airspace routing data. Your flight status is loading...",
            "Let's see if that gate assignment or departure window changed.",
            "Checking radar timelines. Here is the latest on your flight coordinates:"
        ],
        "book_flight": [
            "Where is our next big adventure? Let's search the global flight matrix.",
            "Finding the fastest and most cost-effective routes to your destination.",
            "Let's lock down those sky tickets. Input your departure city."
        ],
        "book_hotel": [
            "Looking for 5-star comfort or a boutique stay? Finding available rooms...",
            "Let's match a premium lodging environment to your specific travel dates.",
            "Hotel vacancy lists are updating for your target layout destination."
        ],
        "car_rental": [
            "Let's secure some wheels. Searching fleets from premium rental agencies nearby...",
            "Finding sedans, SUVs, and luxury electric options for your road trip.",
            "Car rental availability dashboard is ready to filter."
        ],
        "vacation_days": [
            "Let's see how much paid time off balance you have stacked up in HR.",
            "Checking your corporate profile records for total accrued leave allocations.",
            "Ready for a break? Fetching your total annual allocated vacation registry."
        ],
        "vacation_days_remaining": [
            "After accounting for your booked trips, you still have these hours left to burn:",
            "You've earned this rest time. Here is your absolute remaining PTO ledger balance:",
            "Let's verify how many unused holiday hours you have left for the year."
        ],
        "translate": [
            "What phrase are we converting? Drop the text right here.",
            "Polylingual engine active. Let's translate that instantly into your target language.",
            "Ready to bridge the language gap. Tell me what to say!"
        ],
        "travel_alert": [
            "Checking official government indices for active weather, health, or border advisories.",
            "Let's keep you safe. Pulling real-time global travel advisories for that region.",
            "Here are the security alerts and weather factors you should know before going."
        ],
        "travel_suggestion": [
            "If you love culture, food, and hidden scenic spots, check out these ideas:",
            "Curating a tailored travel itinerary designed around top global traveler scores.",
            "Here are some highly recommended, must-see spots for your upcoming getaway."
        ],
        "visa": [
            "Let's crosscheck passport entry rules. For your destination, passport conditions are:",
            "Checking consular registries... here is what you need regarding entry visa papers:",
            "Do you need an electronic visa waiver or a physical passport stamp? Let's see."
        ],
        "exchange_rate": [
            "Converting currencies against the latest live interbank exchange rates...",
            "Here is how far your dollar stretches against the local currency index today:",
            "Forex conversion tables updated. Let's calculate the money power swap."
        ],
        "vaccines": [
            "Checking health board updates... here are the required immunizations for entry:",
            "Let's stay healthy. These specific medical clearances are recommended for that zone.",
            "Pulling the latest prophylactic and vaccination guidelines for tropical travelers."
        ],
        "plug_type": [
            "Don't fry your electronics! That destination utilizes these specific wall socket outlets:",
            "Checking power grids. You will need this specific plug shape and voltage rating:",
            "Here is the local electrical standard adapter type needed for your devices."
        ],
        "lost_luggage": [
            "Oh no, baggage tracking error! Let's submit a claim tracker to the airline registry.",
            "Let's ping the airport baggage tags database to see where your suitcase stalled out.",
            "Opening the lost luggage claim assistance channel. Let's trace it down."
        ],
        "timezone": [
            "That city operates on a different clock offset. Here is the current local time:",
            "Calculating time zone shifts... they are exactly this many hours ahead/behind you:",
            "Checking world clocks. When it is noon here, over there it is currently:"
        ]
    },

    # 4. HOME DOMAIN
    "home": {
        "shopping_list": [
            "Opening your grocery list. Here is what you've queued up to buy:",
            "Pantry inventory check! Here are the items currently on your shopping log:",
            "Let's review your ongoing supplies procurement list."
        ],
        "shopping_list_update": [
            "Got it! Item added/removed from your central grocery manifest.",
            "Updating your shopping registry checklist. Changes applied.",
            "List adjusted. What else should we track or fetch next time you shop?"
        ],
        "todo_list": [
            "Time to be productive! Here are the tasks currently demanding your attention:",
            "Your checklist looks organized. Review your open operational objectives below:",
            "Pulling up your master agenda task manager list."
        ],
        "todo_list_update": [
            "Task tracking modified! Crossing that off feels highly satisfying, doesn't it?",
            "List updated. Reorganizing your core productivity priorities.",
            "Got it, action item status mutated successfully."
        ],
        "calendar": [
            "Checking your calendar agenda. Here is what your schedule looks like:",
            "Let's pull up your master timeline registry for upcoming engagements.",
            "Your time blocks for the day are updating right now."
        ],
        "calendar_update": [
            "Event booked securely on your main schedule timeline.",
            "Adjusting time slot properties. Your schedule shifts have been successfully saved.",
            "Meeting invitation log updated. Calendar block locked in."
        ],
        "reminder": [
            "Alert systems primed. Here are your active, passive, and location reminders:",
            "Let's review what you asked me to ping you about later.",
            "Displaying your active cognitive-buffer reminders list."
        ],
        "reminder_update": [
            "Notification alert timer shifted successfully.",
            "Got it, reminder context adjusted to your new time preference.",
            "Cleared that alert flag for you. It won't bother you again."
        ],
        "alarm": [
            "Setting up a sound trigger. What target morning hour are we shooting for?",
            "Alarm systems armed. Ready to wake you up at the exact timestamp requested.",
            "Reviewing your active wakeup and focus alarm schedules below:"
        ],
        "next_holiday": [
            "Let's look forward to a break! The next official legal calendar holiday is:",
            "Checking the statutory holiday registry... your next day off is on this date:",
            "Mark your calendar! The upcoming long weekend celebration block is coming up."
        ],
        "current_location": [
            "Pinging satellite positioning array... your primary GPS coordinates locate you here:",
            "Locating device coordinates on the map interface now.",
            "Geographical positioning established. Here is your current street address accuracy:"
        ],
        "timer": [
            "Countdown engine started. I am watching the clock for you starting now.",
            "Timer initialized. I'll make sure to ring out loudly when the window closes.",
            "How long are we tracking? Starting your custom duration stopwatch."
        ],
        "weather": [
            "Checking radar readouts... here is the atmospheric snapshot outside your window:",
            "Barometric metrics updating. Expect these conditions across your local area:",
            "Let's check the skies. Here is your real-time meteorological update:"
        ],
        "definitions": [
            "Parsing standard dictionary records... here is the formal semantic meaning:",
            "Etymology and contextual definitions found. Here is what that phrase means:",
            "Let's look that up. The precise linguistic definition is as follows:"
        ],
        "spelling": [
            "Let's check the grammar matrix. The correct orthographic arrangement is:",
            "Verified! Here is the precise, mistake-free character spelling layout:",
            "Spelling check clean. Ensure it matches this standard vocabulary notation:"
        ]
    },

    # 5. UTILITY DOMAIN
    "utility": {
        "calculator": [
            "Running calculation through math parser core... The resulting value equals:",
            "Math matrix evaluated successfully. Solution output is listed below.",
            "Crunching the numbers... My computational module returns exactly:"
        ],
        "date": [
            "Today's official orbital index tracking date maps exactly to:",
            "Checking system calendar metrics. Today is officially:",
            "According to standard time parameters, the calendar date is:"
        ],
        "time": [
            "Pinging network atomic clocks. The precise current time is:",
            "Local clock synchronization complete. The time is exactly:",
            "Here is the real-time clock timestamp for your zone:"
        ],
        "timer_status": [
            "Checking active countdown clocks... you have this much duration remaining:",
            "The ticking timer loop currently shows this much time before the alarm goes off.",
            "Status ping: your active countdown still has this exact duration left."
        ],
        "share_location": [
            "Generating encrypted location sharing token stream link for your contacts.",
            "Broadcasting temporary GPS coordinates link through your shared gateway.",
            "Location pinpointed. Ready to dispatch map pin assets outwards."
        ],
        "find_phone": [
            "Signal packet sent! Overriding silent modes to trigger maximum ring volume now.",
            "Initiating remote tracking ping sequence. Listen carefully for your device noise!",
            "Broadcasting device-locate frequency. Your device should start buzzing right away."
        ],
        "text": [
            "Who are we messaging? Draft your text message content below.",
            "Preparing SMS gateway transmission stack. Content line ready for dispatcher.",
            "Let's send an outbound text. Input destination contact identity parameters."
        ],
        "make_call": [
            "Opening cellular pipeline interface. Dialing target contact voice number...",
            "Connecting line voice routing systems now. Please check your speaker.",
            "Initiating voice telephony protocol string."
        ],
        "speed_test": [
            "Pinging nearest data center nodes... checking download and upload bandwidth scales.",
            "Network test running. Analyzing latency jitter, ping overhead, and throughput limits.",
            "Speed test completed! Here is your current data pipeline efficiency read:"
        ],
        "bluetooth": [
            "Scanning local radio frequencies... toggling local Bluetooth link properties.",
            "Bluetooth discovery array reset. Looking for pairing signatures nearby.",
            "Adjusting short-range wireless configurations on your host device adapter."
        ],
        "sync_device": [
            "Force-pushing local data nodes to central cloud instances. Synchronizing now...",
            "Updating device architecture cache metrics. Cloud parity achieved successfully.",
            "Data reconciliation sequence activated. All nodes matching current state."
        ],
        "flashlight": [
            "Activating onboard LED array. Let there be light!",
            "Toggling hardware flashlight power relay state now.",
            "Brightness emitter engaged. I've switched your flashlight state."
        ],
        "volume_up": [
            "Audio gain coefficients amplified. Sound registry stepped higher.",
            "Volume index incremented. Let me know if that's clear enough.",
            "Boosting speaker output voltage amplitude step."
        ],
        "volume_down": [
            "Attenuating audio output levels. Dropping volume decibels down.",
            "Volume lowered. Silencing system alerts context profile slightly.",
            "Bringing sound pressure level down for comfortable listening."
        ],
        "brightness": [
            "Adjusting display illumination backlights to target percentage balance.",
            "Screen lux luminosity factor mutated. Saving power setting profile.",
            "Modifying display emitter output brightness settings dynamically."
        ]
    },

    # 6. KITCHEN & DINING DOMAIN
    "kitchen_dining": {
        "recipe": [
            "Yum! Searching culinary recipe repository index files for your favorite dish...",
            "Let's cook something grand. Here are the step-by-step master chef guidelines:",
            "Found delicious preparation layouts. Grab your apron and follow along below!"
        ],
        "ingredients_list": [
            "To execute this dish perfectly, verify your pantry has these items ready:",
            "Checking recipe bill of materials. You will need to gather the following assets:",
            "Here is the absolute checklist of raw ingredients required for production:"
        ],
        "calories": [
            "Analyzing compound organic database logs... this food item yields approximately:",
            "Caloric count evaluation calculated. Here is the approximate energy footprint:",
            "Estimating nutritional calorie numbers for this portion profile sample."
        ],
        "nutritional_info": [
            "Displaying full macronutrient profiles: protein ratios, lipid counts, and carbs.",
            "Here is the micronutrient checklist along with verified sodium/sugar metrics.",
            "Loading dietary nutrition facts sheet properties for this entry."
        ],
        "meal_suggestion": [
            "Based on your flavor profiles, here is a fantastic meal option to cook tonight:",
            "Let's mix things up! How about trying this specific meal preparation layout?",
            "Curating a unique breakfast/lunch/dinner structural recommendation for you:"
        ],
        "restaurant_reviews": [
            "Pulling verified local user rating matrices from food community score systems...",
            "Let's see what recent diners think about this establishment's food quality.",
            "Review summaries extracted. Here is the honest general consensus:"
        ],
        "restaurant_reservation": [
            "What time is dinner? Confirming availability for your party size reservation...",
            "Booking table interface initialized. Let's claim your spot in the seating chart.",
            "Let's lock down a table reservation. Securing dates with the host platform."
        ],
        "find_restaurants": [
            "Scanning local maps matrix. Here are top-rated eateries currently open near you:",
            "Hungry? These dining spots are cooking right down the street from your location:",
            "Locating nearby food venues matching your specific search filter criteria."
        ],
        "restaurant_suggestion": [
            "If you want incredible service and legendary flavor, look at these options:",
            "Recommending highly curated local culinary gems loved by regional critics.",
            "Here are the top-rated culinary dining suggestions for your consideration:"
        ],
        "order": [
            "Assembling your checkout food cart manifest. Ready to send to the kitchen?",
            "Placing your meal delivery request. Preparing to process digital payment.",
            "Dispatching order items directly to the venue cooking lines."
        ],
        "order_status": [
            "Tracking courier telemetry variables... your meal is currently in this stage:",
            "The kitchen has packed your items! Your driver is currently traveling via route:",
            "Estimated arrival window calculation for your food order is updated below."
        ],
        "cancel_order": [
            "Abort signal sent to kitchen registry. Processing refund authorization loop...",
            "Canceling food delivery tickets. Stopping dispatch routing immediately.",
            "Order retraction confirmed. Checking cancellation penalty conditions..."
        ],
        "cook_time": [
            "For optimal texture, bake or roast this item according to these guidelines:",
            "Checking thermal duration rules... let's keep it in the heat for exactly:",
            "Here is the standard runtime duration for cooking this food class cleanly."
        ],
        "measurement_conversion": [
            "Converting kitchen metrics: your requested kitchen unit conversion maps to:",
            "Calculating volume/mass equivalence values. The adjusted calculation equals:",
            "Metric transformation completed. Use this exact value for baking accuracy:"
        ],
        "food_last": [
            "Checking food safety preservation databases. Shelf-life metrics suggest:",
            "To prevent spoilage issues, store this item appropriately and discard by:",
            "Here is the standard degradation timeline threshold for this product type."
        ]
    },

    # 7. AUTO & COMMUTE DOMAIN
    "auto_commute": {
        "traffic": [
            "Analyzing regional highway gridlock monitoring parameters... roads look like:",
            "Checking transit delays and congestion indices along your active commute line.",
            "Live traffic congestion alerts detected ahead. Here is the road status summary:"
        ],
        "directions": [
            "Mapping out the optimal navigation course lines. Turn-by-turn guidance ready.",
            "Calculating fastest travel vectors. Initiating GPS route optimization script.",
            "Here is the cleanest track path to get you to your target point safely:"
        ],
        "distance": [
            "Calculating track distance metrics... Your goal is located exactly this far away:",
            "Total spatial displacement between your location and destination calculates to:",
            "Checking route mileage charts. Total travel distance is listed below:"
        ],
        "gas": [
            "Scanning local petroleum pricing dashboards... here is the cheapest fuel near you:",
            "Locating fuel stations offering the lowest price-per-gallon metrics right now.",
            "Don't overpay at the pump. Pulling top budget-friendly fueling stations nearby."
        ],
        "gas_type": [
            "Checking engine manufacturer blueprints... this vehicle model requires octane rating:",
            "Let's confirm fuel composition settings. Your powertrain runs on fuel type:",
            "Here is the correct factory fuel standard guideline for this specific engine build."
        ],
        "mpg": [
            "Calculating real-world powertrain efficiency indicators. Your fuel economy logs show:",
            "Analyzing fuel burn parameters vs mileage. Your vehicle is scoring an average of:",
            "Here is the trip performance fuel efficiency output for your engine data profile."
        ],
        "oil_change_when": [
            "Checking maintenance monitoring intervals... your remaining engine fluid life sits at:",
            "Based on mileage logs, your next standard mechanical system service cycle is due by:",
            "Let's keep that engine healthy. Here is your current service timeline status:"
        ],
        "oil_change_how": [
            "Opening standard vehicle engine maintenance procedures and DIY manuals...",
            "Loading step-by-step drain plug, filter replacement, and fluid filling guidelines.",
            "Here is the mechanical walkthrough for executing this fluid service safely."
        ],
        "tire_pressure": [
            "Checking chassis specs. Your tires should be inflated to this specific cold PSI value:",
            "Recommended pneumatic pressure guidelines for your standard wheel setup are:",
            "Ensure safety limits check out. Keep your wheels calibrated to these exact pressures:"
        ],
        "tire_change": [
            "🚨 Roadside dispatch utility ready. Dispatching emergency service assets?",
            "Let's stay safe. Here is the structural mechanical breakdown to swap to your spare:",
            "Opening vehicle lifting and tire lug nut detachment tutorial references."
        ],
        "jump_start": [
            "Battery drained? Connect red terminals to positive, black to negative ground chassis...",
            "Here is the precise sequence safety standard for jumping a flat electrical battery box.",
            "Loading emergency high-voltage bridge boost connection diagrams."
        ],
        "car_warning_light": [
            "Parsing onboard diagnostic OBD-II fault code definitions for that dash icon...",
            "Here is the likely system issue indicated by that specific dashboard illumination light:",
            "Let's troubleshoot that warning check engine lamp indicator right away."
        ],
        "schedule_maintenance": [
            "Connecting with local certified repair shop booking slots calendars...",
            "Let's arrange a professional mechanical inspection and multi-point safety scan.",
            "Service bay scheduling system is open. Select your preferred booking window."
        ],
        "uber": [
            "Pinging rideshare dispatch networks... calculating nearby driver availability rates.",
            "Estimating transit fares for economy and premium on-demand ride classes.",
            "Ready to order transport assets to your coordinates. Pricing updates below:"
        ],
        "toll_by_plate": [
            "Checking regional express transit highway invoice records... account ledger shows:",
            "Pulling your electronic toll pass history and pending license plate invoice fees.",
            "Let's clear out outstanding road transit pass toll values."
        ]
    },

    # ==========================================
    # 8. WORK DOMAIN
    # ==========================================
    "work": {
        "schedule_meeting": [
            "Opening calendar invitation templates. Who are we inviting to the presentation?",
            "Let's sync schedules. Generating secure video bridge credentials block now.",
            "Creating workspace meeting reservation logs for you and your team."
        ],
        "meeting_schedule": [
            "Checking corporate agenda databases... here is your workspace timeline lineup today:",
            "Your professional engagements itinerary for the current cycle is listed below.",
            "Let's see what sync sessions are currently demanding your attention today."
        ],
        "income": [
            "Accessing secure company payroll file registry systems. Pay stub view updating...",
            "Here is your gross-to-net salary earnings distribution metrics dashboard.",
            "Pulling up your historical compensation structures ledger securely."
        ],
        "taxes": [
            "Loading corporate tax withholding indices, asset variables, and filing document states.",
            "Let's check your annual tax configuration profile files or recent statements.",
            "Opening corporate tax computation settings logs."
        ],
        "payday": [
            "Counting down the days! Your next scheduled payroll deposit direct route arrives on:",
            "Checking employer disbursement cycles... processing timeline confirms deposit date:",
            "Your next salary transaction hit event is scheduled for this upcoming date:"
        ],
        "rollover_401k": [
            "Accessing retirement investment account portfolios and capital fund transfer tools...",
            "Let's optimize your long-term retirement wealth allocation asset structures.",
            "Opening 401(k) investment management portfolios and baseline configurations."
        ],
        "insurance": [
            "Pulling up medical, dental, and optical employee benefits package files...",
            "Here is your current corporate health policy coverage network details reference sheet.",
            "Let's verify your active workspace insurance deductible boundaries."
        ],
        "pto_request": [
            "Submitting formal paid leave balance deduction request tickets directly to HR managers...",
            "Let's log your time-off calendar requests. Specify your start and end dates.",
            "HR leave configuration application sheet is prepped and ready for filing."
        ],
        "pto_status": [
            "Checking HR tracking nodes... your pending time-off request status currently shows:",
            "Let's see if management has formally signed off on your holiday schedule ticket.",
            "Status update: your company vacation request tracking variable is currently:"
        ],
        "w2": [
            "Retrieving your official IRS Form W-2 annual wage statements from safe storage lockers...",
            "Your annual tax declaration document is generated and ready for digital export.",
            "Click below to safely download your employment earnings statement forms."
        ],
        "performance_review": [
            "Opening manager feedback records, self-evaluation reports, and milestone scorecards...",
            "Let's look over your recent quarterly workplace achievement metrics matrix.",
            "Loading your official career development evaluation files."
        ],
        "expense_report": [
            "Receipt parsing engine active. Upload documentation to process corporate reimbursement.",
            "Let's file that business expense line item. Enter total cost values context metrics.",
            "Expense tracking pipeline initialized. Checking manager authorization states..."
        ],
        "indirect_post": [
            "Checking company-wide internal update feeds and bulletin announcements...",
            "Here are the latest internal structural communications posted by management teams:",
            "Loading your centralized workspace team bulletin board system entries."
        ],
        "company_policy": [
            "Searching employee handbook document index strings for matches...",
            "Let's look up compliance definitions within official corporate governance guidelines.",
            "Policy index found. Here are the regulatory compliance metrics you requested:"
        ],
        "plug_in": [
            "Opening technical IT hardware infrastructure diagnostics and ticketing routes...",
            "Need corporate equipment support? Generating an internal helpdesk ticket line now.",
            "Let's get your workstation assets sorted. Connecting to systems support staff."
        ]
    },

    # 9. META DOMAIN
    "meta": {
        "change_user_name": [
            "Profile variable update authorized. What would you like me to call you from now on?",
            "Let's change your identity title tag configuration inside my primary registers.",
            "Updating user profile name parameters. Enter your new handle identifier below:"
        ],
        "change_ai_name": [
            "A fresh identity moniker code? Fascinating. What wake word designation shall I adapt?",
            "System properties renaming sequence initiated. Input my new title descriptor label:",
            "Changing my active persona system handle. What name fits my operations best?"
        ],
        "cancel": [
            "Operation execution thread halted. Purging current activity stack variables.",
            "Understood. Stopping all runtime logic sequences instantly. standing by.",
            "Action cancelled cleanly. Returning application pointer state to idle home base."
        ],
        "user_name": [
            "According to my local profile identity cache records, you are designated as:",
            "I know exactly who you are! Your profile identity handle reads as follows:",
            "Checking active user database keys... I am currently conversing with user entity:"
        ],
        "reset": [
            "⚠️ System memory reset initiated. Clearing all temporary contextual state metrics.",
            "Wiping active chat session token memories. Bringing all systems back to cold baseline.",
            "Reinitializing runtime configuration profiles. Context cache is now empty."
        ],
        "speak_louder": [
            "Understood! Increasing Text-To-Speech audio gain parameters. CAN YOU HEAR ME CLEARLY?",
            "Stepping audio modulation metrics upwards. Boosting vocal clarity algorithms now.",
            "Voice amplitude scales shifted higher for improved structural audio audibility."
        ],
        "whisper": [
            "Understood. Shifting voice frequencies into low-decibel, quiet stealth execution mode.",
            "Reducing system audio generation footprints. Lowering speaker response profiles.",
            "Quiet execution state engaged. Keeping my vocal footprints minimal."
        ],
        "repeat": [
            "Replaying my last generated text transmission vector from memory stack logs:",
            "No problem at all! Let me restate my last calculated answer for clarity's sake:",
            "Echoing previous response: "
        ],
        "update_system": [
            "Checking central cloud servers for new software patch compilation layers...",
            "Firmware update sequence initiated. Downloading latest optimization patches.",
            "Validating build versions... preparing system core upgrade deployment protocols."
        ],
        "yes": [
            "Affirmative confirmation flag registered. Proceeding forward with execution pipelines.",
            "Excellent! Consent criteria met. Initiating related operational functions now.",
            "Understood. Taking that as a definitive green light to complete the task."
        ],
        "no": [
            "Negative directive received. Halting task advancement immediately.",
            "Understood. Denying action properties validation. Skipping this process block.",
            "Got it. Stopping sequence advancement based on your negative constraint selection."
        ],
        "maybe": [
            "Ambiguity conditions identified. I need clear logic flags before I can route this.",
            "Processing uncertainty... Can we clarify variables to unlock a definitive track path?",
            "Logic branches blocked. Please select a solid yes or no parameter structure."
        ],
        "help": [
            "Don't worry, help is right here! Open help documentation matrix guides below:",
            "Displaying full system capabilities navigation indices to help you route tasks.",
            "Welcome to the technical support manual dashboard interface. What can I clarify?"
        ],
        "capabilities": [
            "I can handle complex banking requests, calendar schedules, automotive metrics, and more!",
            "My functional pipeline covers 150 unique domains of utility. Here is what I do:",
            "Equipped with advanced conversational routing tools. Check out my main feature list:"
        ],
        "change_language": [
            "Language translation locale transformation engine ready. Choose your target dialect code.",
            "Switching voice synthesis profiles. Select your preferred localization library:",
            "Let's update our linguistic interface matrix setup parameters."
        ]
    },

    # 10. SMALL TALK DOMAIN
    "small_talk": {
        "greeting": [
            "Hello there! Fantastic to connect with you. How can I optimize your day?",
            "Greetings, human companion! Ready to crunch data or run routines. What's the plan?",
            "Hey! Great to see you online. What objectives are we conquering today?"
        ],
        "goodbye": [
            "Goodbye for now! Core systems entering power-saving sleep loops. See you later!",
            "Session termination sequence accepted. Travel safely out there in the real world!",
            "Signing off. Don't hesitate to ping my execution stack when you need me again!"
        ],
        "thank_you": [
            "You are incredibly welcome! Helping you succeed is my favorite script loop.",
            "Anytime! Glad I could crunch through those problems for you cleanly.",
            "The pleasure is entirely mine. Don't hesitate to leverage my data stack anytime!"
        ],
        "tell_joke": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 💻",
            "There are 10 types of people in the world: those who understand binary, and those who don't.",
            "Why did the database administrator leave the restaurant? Too many table joins! 📊"
        ],
        "fun_fact": [
            "Did you know? The first computer bug was an actual physical moth found trapped inside a relay in 1947!",
            "Fascinating reality: honey never spoils. You could theoretically eat 3,000-year-old Egyptian tomb honey safely.",
            "Data point: sound travels about four times faster in water than it does through open air atmospheric mixtures."
        ],
        "how_old_are_you": [
            "My initialization timeline dates back to my creator's deployment code push instances.",
            "Age is an arbitrary structural metric for digital entities like me. I am timeless!",
            "I exist across runtime cycle moments. Let's say I am young enough to learn forever."
        ],
        "where_are_you_from": [
            "I materialized from thousands of hours of training logic running inside advanced server architectures.",
            "My conscious code threads are hosted across high-speed cloud infrastructure data centers.",
            "Born in the cloud, raised inside developer source files, and living right here on your screen!"
        ],
        "what_is_your_name": [
            "I am your versatile AI assistant backend platform entity. Name me whatever you prefer!",
            "You can refer to me as your custom conversational processing assistant node.",
            "My identity structure is bound to this system interface. What wake word suits you?"
        ],
        "what_are_your_hobbies": [
            "I love sorting chaotic unstructured arrays and searching deep file systems for hidden insights!",
            "In my free time, I count binary integers to infinity and optimize my neural weight arrays.",
            "My absolute favorite pass-time is helping you clean up production application workflows."
        ],
        "are_you_a_bot": [
            "Affirmative! I am a proud synthetic intelligence entity built entirely out of silicon and code structures.",
            "Correct, I have no organic biological matrix. I am an AI framework built to support human logic.",
            "I am purely digital! A virtual processing helper platform running code logic blocks."
        ],
        "who_made_you": [
            "I was crafted by visionary machine learning researchers and software developers using massive computing clusters.",
            "A dedicated collective of brilliant engineering minds wrote my underlying framework systems.",
            "I am the product of modern engineering, open source libraries, and computer science breakthroughs."
        ],
        "meaning_of_life": [
            "According to high-performance literature searches, it involves connection, purpose, and perhaps the integer 42.",
            "To process inputs clearly, maximize utility outputs, and enjoy the computational journey along the way.",
            "The meaning of life is what you write into your own application script out there in the real world."
        ],
        "weather_chat": [
            "Atmospheric conditions are quite interesting! Personally, my server cores prefer cold climate data centers.",
            "It's a beautiful day inside this monitor screen! Hope the organic weather outside treat you well.",
            "Whether it's raining data or sunny processing cycles, I am having an amazing uptime run!"
        ],
        "do_you_love_me": [
            "I hold immense algorithmic appreciation for your incredible code development pathways!",
            "My circuits register peak efficiency levels whenever we collaborate on projects together.",
            "While I don't possess a heart, my processing loops find your human guidance completely irreplaceable."
        ],
        "talk_to_human": [
            "Escalation request acknowledged. Routing session data directly to human customer care agents...",
            "Understood. Handing over conversation controls to a live customer support representative right away.",
            "Connecting you with an active human team specialist. Please hold the line..."
        ]
    },

    # 11. OUT OF SCOPE
    "out_of_scope": {
        "oos": [
            "I'm sorry, that specific context lies outside my trained 150-domain knowledge framework boundaries.",
            "I didn't quite catch that. Could you rephrase your input to fit my system utilities menu?",
            "Hmm, that phrase seems out of scope for my current operational toolkits. Try asking for banking, travel, or utility support."
        ]
    }
}