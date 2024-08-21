from fastapi import FastAPI

app = FastAPI()

@app.post("/signup")
def signup():
    
    return {
        "message" : "회원가입 성공"
    }
    
@app.post("/login")
def login():
    return {
        "message": "로그인 성공",
        "token": {'jwt 토큰'},
        "user" : "string"
    }
    
@app.delete("/delete")
def delete_user(uid):
    return {
        "message": "User deleted successfully"
    }
    
@app.get("/tickets")
def get_tickets():
    return {
        {
            "totalItems": number,
            "totalPages": number,
            "currentPage": number,
            "tickets": [
            {
            "id": number,
            "departure": "대한민국",
            "departure_airport": "인천국제공항",
            "departure_airport_code": "ICN",
            "destination": "일본",
            "destination_airport": "도쿄 나리타 공항",
            "destination_airport_code": "NRT",
            "departure_date": "2024-05-01",
            "destination_date": "2024-05-01",
            "departure_time": "10:00",
            "destination_time": "14:00",
            "duration": "4시간",
            "airline": "대한항공",
            "flightClass": "이코노미",
            "price": 500000
            }
            ]
        }
    }
    
@app.post("/purchase")
def purchase_ticket(tid):
    return {
        "message": "구매 완료",
        "ticket": {
        "id": number,
        "departure": "대한민국",
        "departure_airport": "인천국제공항",
        "departure_airport_code": "ICN",
        "destination": "일본",
        "destination_airport": "도쿄 나리타 공항",
        "destination_airport_code": "NRT",
        "departure_date": "2024-05-01",
        "destination_date": "2024-05-01",
        "departure_time": "10:00",
        "destination_time": "14:00",
        "duration": "4시간",
        "airline": "대한항공",
        "flightClass": "이코노미",
        "price": 500000
        }
    }

@app.post("/tickets/refund")
def refund_ticket(tid):
    return {
        "message": "티켓이 환불되었습니다."
    }

@app.post("/change-password")
def change_password(uid):
    return {
         "message": "비밀번호가 변경되었습니다."
    }       
    
@app.get("/flights")
def get_flights():
    return {
        "totalItems": number,
        "totalPages": number,
        "currentPage": number,
        "flights": [
            {
            "id": number,
            "departure": "대한민국",
            "departure_airport": "인천국제공항",
            "departure_airport_code": "ICN",
            "destination": "일본",
            "destination_airport": "도쿄 나리타 공항",
            "destination_airport_code": "NRT",
            "departure_date": "2024-05-01",
            "destination_date": "2024-05-01",
            "departure_time": "10:00",
            "destination_time": "14:00",
            "duration": "4시간",
            "airline": "대한항공",
            "flightClass": "이코노미",
            제목 없음 7
            "price": 500000
            }
        ]
    }
