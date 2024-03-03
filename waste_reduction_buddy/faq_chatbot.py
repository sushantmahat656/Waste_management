from fuzzywuzzy import fuzz

class FAQChatbot:
    FAQ_DATABASE = [
        {'question': 'What is WasteBuddy?', 'answer': 'WasteBuddy is a waste management platform that helps in makeing earth a cleaner place.'},
        {'question': 'How can I book an appointment?', 'answer': 'You can book an appointment on the homepage.'},
        
    ]



    
    def get_answer(question):

        if question.lower() in ['hi', 'hello', 'hey','namaste']:
            return "Hello! I'm your WasteBuddy chatbot. Feel free to ask me any questions about WasteBuddy.like:What is WasteBuddy? or  How can I book an appointment?"

        best_match = None
        max_ratio = 0

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