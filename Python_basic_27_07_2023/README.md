# Object Detection Using Yolov8 
Object Detection Using Yolov8 will take the image as input and return the objects and thier probability as Json response.
## Setup
  ```code
  conda create -n <env_name>
  conda activate <env_name>
  git clone https://github.com/USTAADCOM/Internship_task_repo.git
  cd Python_basic_27_07_2023
  pip install -r requirements.txt
  ```
## Project Structure
```bash
AWS_Lambda_API
   │   lambda_function.py
   │   test_encryption_decyption.py
   │   test_frequency_counter.py
   │   test_pladirme_checker.py
   │   test_prime_checker.py
   │   test_word_counter.py
   ├───module
       |  ceasrer_cipher_encryption_decryption.py
       │   pladirme_checker.py
       │   prime_checker.py
       │   word_counter.py
       │   word_frequency_counter.py
```

## Word Counter 
Payload
Form Data
```code
Key: image_file  value: Image path
```
Header 
```code
key: api-key     value: pakistan
```
![Alt text](image.png) 
Response 
```code
{
    "object1": {
        "confidence": 0.89,
        "object": "person",
        "shape_box": [
            254,
            206,
            896,
            1664
        ]
    }
}
```
![Alt text](image-1.png)
