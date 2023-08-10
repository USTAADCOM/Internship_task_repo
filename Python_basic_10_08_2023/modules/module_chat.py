"""
module contain the model loading and create the response functionalities.
"""
import pickle
def load_model_gpt2():
    """
    method will load the model and return loaded model model_GPT2.

    Parameters:
    ----------
    None

    Return:
    ------
    model: Any
        return the model object loaded from model_GPT2.pkl file.

    """
    model = pickle.load(open('/content/ChatBot/model_GPT2.pkl','rb'))
    return model

def load_gpt2_tokenizer():
    """
    method will load the model and return loaded model tokenizer_GPT2.

    Parameters:
    ----------
    None

    Return:
    ------
    model: Any
        return the model object loaded from tokenizer_GPT2.pkl file.

    """
    model_tokenizer = pickle.load(open('/content/ChatBot/tokenizer_GPT2.pkl','rb'))
    return model_tokenizer

def get_chat_response(text_data: str)-> dict:

    """
    method will take the text_data and return its converstaional response by using the
    GPT2 model.

    Parameters:
    ----------
    text_data: str
      text data contain the message send by the user to the chatbot.

    Return:
    ------
    str
        return the last response send by the chatbot as a string.

    """
    model = None
    tokenizer = None
    # for step in range(6):
    #     # encode the new user input, add the eos_token and return a tensor in Pytorch
    #     new_user_input_ids = tokenizer.encode(str(text_data) + tokenizer.eos_token, return_tensors = 'pt')
    #     # append the new user input tokens to the chat history
    #     bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim = -1) if step > 0 else new_user_input_ids
    #     # generated a response while limiting the total chat history to 1000 tokens,
    #     chat_history_ids = model.generate(bot_input_ids, max_length = 1000, pad_token_id = tokenizer.eos_token_id)
    #     # pretty print last ouput tokens from bot
    #     return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens = True)