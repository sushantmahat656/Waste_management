from fuzzywuzzy import fuzz

class FAQChatbot:
    FAQ_DATABASE = [
        {'question': 'Appointment', 'answer': 'You can book an appointment on the homepage.'},
        {'question': 'What is WasteBuddy?', 'answer': 'WasteBuddy is a waste management platform that helps in making earth a cleaner place.'},
        {'question': 'How can I book an appointment?', 'answer': 'You can book an appointment on the homepage.'},
        {'question': 'How do I sign up for WasteBuddy?', 'answer': 'You can sign up for WasteBuddy by visiting our website and clicking on the "Register" button.'},
        {'question': 'What services does WasteBuddy provide?', 'answer': 'WasteBuddy provides various waste management services such as recycling, composting, and waste disposal.'},
        {'question': 'Is WasteBuddy available in my area?', 'answer': 'WasteBuddy is available in select areas. Please check our website or contact us to see if we operate in your area.'},
        {'question': 'How can I contact WasteBuddy?', 'answer': 'You can contact WasteBuddy by filling out the contact form on our website or by calling our customer support hotline.'},
        {'question': 'What are the benefits of using WasteBuddy?', 'answer': 'Using WasteBuddy helps reduce environmental pollution, conserve natural resources, and promote sustainable waste management practices.'},
        {'question': 'Can I schedule recurring appointments with WasteBuddy?', 'answer': 'NO, you cannot schedule recurring appointments for waste collection or other services with WasteBuddy.'},
        {'question': 'How can I cancel my appointment with WasteBuddy?', 'answer': 'You cannot cancel your appointment with WasteBuddy but you can contact us to cancel the appointments.'},
        {'question': 'Does WasteBuddy offer discounts for bulk waste disposal?', 'answer': 'Yes, WasteBuddy offers discounts for bulk waste disposal. Please contact us for more information.'},
        {'question': 'How does WasteBuddy ensure responsible waste disposal?', 'answer': 'WasteBuddy follows strict guidelines and regulations to ensure responsible waste disposal, including proper sorting, recycling, and disposal methods.'},
        {'question': 'What types of waste does WasteBuddy accept?', 'answer': 'WasteBuddy accepts various types of waste, including household waste, electronic waste, organic waste, and more. Please check our website for a complete list of accepted items.'},
        {'question': 'Does WasteBuddy provide waste collection for businesses?', 'answer': 'Yes, WasteBuddy provides waste collection and management services for businesses of all sizes.'},
        {'question': 'Can I track the status of my appointment with WasteBuddy?', 'answer': 'Yes, you can track the status of your appointment with WasteBuddy by logging into your account on our website.'},
        {'question': 'Does WasteBuddy offer educational programs on waste management?', 'answer': 'Yes, WasteBuddy offers educational programs and resources on waste management for schools, businesses, and community groups.'},
        {'question': 'How can I report a problem with WasteBuddy service?', 'answer': 'You can report a problem with WasteBuddy service by contacting our customer support team or filling out the feedback form on our website.'},
        {'question': 'Does WasteBuddy offer composting services?', 'answer': 'Yes, WasteBuddy offers composting services for organic waste. Contact us to learn more about our composting program.'},
        {'question': 'Can I request a special pickup with WasteBuddy?', 'answer': 'Yes, you can request a special pickup for large items or unusual waste materials with WasteBuddy.'},
        {'question': 'What are WasteBuddys operating hours?', 'answer': 'WasteBuddys operating hours vary by location and service. Please check our website or contact us for specific operating hours in your area.'},
            
    ]

    def get_answer(question):

        if question is not None:

            best_match = None
            max_ratio = 0

            if question.lower() in ['hi', 'hello', 'hey','namaste']:
                return "Hello! I'm your WasteBuddy chatbot. Feel free to ask me any questions about WasteBuddy."

            for faq in FAQChatbot.FAQ_DATABASE:
                ratio = fuzz.token_sort_ratio(question.lower(), faq['question'].lower())
                if ratio > max_ratio:
                    max_ratio = ratio
                    best_match = faq

            if max_ratio > 60:  
                return best_match['answer']
            else:
                # Default response when no matching question is found
                return "I'm sorry, but I couldn't find information related to that question. Feel free to ask me about WasteBuddy, like 'What is WasteBuddy?' or 'How can I book an appointment?'"

# Example usage:
# question = "What is WasteBuddy?"
# answer = FAQChatbot.get_answer(question)