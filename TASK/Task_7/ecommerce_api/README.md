# E‑Commerce API (Routers + JWT + Timing) 
## Features
* Register/Login → Get JWT token

* Browse Products → Search/filter categories

* Add to Cart → Manage items

* Checkout → Create order & pay

* Track Orders → View status history
and can be extended to

    * Leave Reviews → Rate purchased products

## Folder Structure
ecommerce_api/
├─ main.py
├─ database.py
├─ models.py
├─ auth.py
├─ routers/
│  ├─ products.py
│  ├─ cart.py
│  └─ users.py
├─ middleware.py
├─ orders.json
├─ README.md
└─ requirements.txt

## App Setup
```bash
git clone <repo-url>
cd Task_7
pip install -r requirements.txt
```

## Run app
```bash
uvicorn ecommerce_api.main:app --reload
```