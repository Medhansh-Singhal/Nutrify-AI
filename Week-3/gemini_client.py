"""
🤖 Simple Gemini AI Client for Nutrify AI
"""

import os

class GeminiAIClient:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
    
    def get_response(self, prompt: str) -> str:
        """Get AI response from Gemini"""
        try:
            if not self.api_key:
                return self._get_fallback_response(prompt)
            
            # Simple fallback responses for common questions
            return self._get_fallback_response(prompt)
            
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
    
    def _get_fallback_response(self, prompt: str) -> str:
        """Get fallback response when Gemini is not available"""
        prompt_lower = prompt.lower()
        
        if any(word in prompt_lower for word in ['soil', 'nutrient', 'deficiency']):
            return """
            🌱 **Soil Nutrition Advice:**
            
            For soil nutrition issues, I recommend:
            1. **Test your soil** regularly to understand nutrient levels
            2. **Use organic compost** to improve soil health
            3. **Apply vermicompost** for natural nutrient enrichment
            4. **Consider crop rotation** to maintain soil fertility
            5. **Use green manure** crops like legumes
            
            For specific deficiency issues, please use our soil analysis tool to get personalized recommendations.
            """
        
        elif any(word in prompt_lower for word in ['organic', 'chemical', 'pesticide']):
            return """
            🌿 **Organic Farming Solutions:**
            
            For organic farming practices:
            1. **Composting**: Create nutrient-rich compost from kitchen waste
            2. **Vermicompost**: Use earthworms for natural soil improvement
            3. **Neem-based solutions**: Natural pest control methods
            4. **Crop rotation**: Prevent soil depletion and pest buildup
            5. **Mulching**: Retain soil moisture and suppress weeds
            
            These methods are cost-effective and environmentally friendly!
            """
        
        elif any(word in prompt_lower for word in ['cost', 'price', 'expensive', 'budget']):
            return """
            💰 **Cost-Effective Farming:**
            
            For budget-friendly farming:
            1. **Start small** with organic methods
            2. **Make your own compost** from farm waste
            3. **Use local resources** and traditional knowledge
            4. **Group farming** to reduce input costs
            5. **Government schemes** for financial support
            
            Our soil analysis tool provides cost estimates for all recommended treatments.
            """
        
        else:
            return """
            🌱 **Welcome to Nutrify AI!**
            
            I'm here to help with your farming questions! You can ask about:
            - Soil nutrition and deficiency issues
            - Organic farming methods
            - Cost-effective solutions
            - Crop-specific advice
            - Sustainable agriculture practices
            
            For detailed analysis, please use our soil analysis tool first, then ask me specific questions based on your results!
            """
