# SecureBank
Django app to fetch bank details

Hosted on https://deepsecurebank.herokuapp.com/

**NOTE:** You will get `Server Error (500)` while trying to access the URL, as it requires authentication token.

## Application Details:

**Dataset:** https://github.com/snarayanank2/indian_banks 

Use `curl` to fetch bank details from server. Refer examples below:

```
> out=$(curl -X POST -H "Content-Type: application/json" -d '{"username": "mandeep", "password": "mandeep"}' https://deepsecurebank.herokuapp.com/api/token/)

> echo $out
{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU2NDc1MzAzNywianRpIjoiODAzNDkzMWM0ZGZiNGQyYzlkMTE1M2VmMzliNTMwOTAiLCJ1c2VyX2lkIjoxfQ.iwbe-sDEViCdTxlAN48fEjTaL-H9YCtrB2QUnbAdovE","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY0MzIxMDM3LCJqdGkiOiJlMGQ3NjMwM2Q3ZWY0MzUwYTQ5NTgwOWZhYWNiM2VhNCIsInVzZXJfaWQiOjF9.snne4DwHuU1LxekM7WKPMeoQR435AmNXUwqiqm575vM"}

> access=$(jq -r ".access" <<<"$out")
> refresh=$(jq -r ".refresh" <<<"$out")

Return two enteris after skipping first 3 for given bankname and cityname
> curl -H "Authorization: Bearer $access" https://deepsecurebank.herokuapp.com/fetchbank/bankname\=ABHYUDAYA+COOPERATIVE+BANK+LIMITED\&cityname\=MUMBAI\&limit\=2\&offset\=3/
[{"ifsc":"ABHY0065004","bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED","branch":"BHANDUP","address":"CHETNA APARTMENTS, J.M.ROAD, BHANDUP, MUMBAI-400078","district":"GREATER MUMBAI","city":"MUMBAI","state":"MAHARASHTRA"},{"ifsc":"ABHY0065005","bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED","branch":"DARUKHANA","address":"POTIA IND.ESTATE, REAY ROAD (E), DARUKHANA, MUMBAI-400010","district":"GREATER MUMBAI","city":"MUMBAI","state":"MAHARASHTRA"}]

Return first 4 enteries for given bankname and cityname
> curl -H "Authorization: Bearer $access" https://deepsecurebank.herokuapp.com/fetchbank/bankname\=ABHYUDAYA+COOPERATIVE+BANK+LIMITED\&cityname\=MUMBAI\&limit\=4/
[{"ifsc":"ABHY0065001","bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED","branch":"RTGS-HO","address":"ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024","district":"GREATER MUMBAI","city":"MUMBAI","state":"MAHARASHTRA"},{"ifsc":"ABHY0065002","bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED","branch":"ABHYUDAYA NAGAR","address":"ABHYUDAYA EDUCATION SOCIETY, OPP. BLDG. NO. 18, ABHYUDAYA NAGAR, KALACHOWKY, MUMBAI - 400033","district":"GREATER MUMBAI","city":"MUMBAI","state":"MAHARASHTRA"},{"ifsc":"ABHY0065003","bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED","branch":"BAIL BAZAR","address":"KMSPM'S SCHOOL, WADIA ESTATE, BAIL BAZAR-KURLA(W), MUMBAI-400070","district":"GREATER MUMBAI","city":"MUMBAI","state":"MAHARASHTRA"},{"ifsc":"ABHY0065004","bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED","branch":"BHANDUP","address":"CHETNA APARTMENTS, J.M.ROAD, BHANDUP, MUMBAI-400078","district":"GREATER MUMBAI","city":"MUMBAI","state":"MAHARASHTRA"}]

Return all the enteries for given bankname and cityname
> curl -H "Authorization: Bearer $access" https://deepsecurebank.herokuapp.com/fetchbank/bankname\=ABHYUDAYA+COOPERATIVE+BANK+LIMITED\&cityname\=MUMBAI/
[{"ifsc":"ABHY0065001","bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED","branch":"RTGS-HO","address":"ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024","district":"GREATER MUMBAI","city":"MUMBAI","state":"MAHARASHTRA"}......

For /fetchifsc/, it can return maximum of 1 entry as IFSC code is unique for each bank,eg. If you specify offset>0, it will return []
> curl -H "Authorization: Bearer $access" https://deepsecurebank.herokuapp.com/fetchifsc/ifsc\=ABHY0065002\&limit\=2/
[{"ifsc":"ABHY0065002","bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED","branch":"ABHYUDAYA NAGAR","address":"ABHYUDAYA EDUCATION SOCIETY, OPP. BLDG. NO. 18, ABHYUDAYA NAGAR, KALACHOWKY, MUMBAI - 400033","city":"MUMBAI","district":"GREATER MUMBAI","state":"MAHARASHTRA"}]

> curl -H "Authorization: Bearer $access" https://deepsecurebank.herokuapp.com/fetchifsc/ifsc\=ABHY0065002\&limit\=2\&offset\=0/
[{"ifsc":"ABHY0065002","bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED","branch":"ABHYUDAYA NAGAR","address":"ABHYUDAYA EDUCATION SOCIETY, OPP. BLDG. NO. 18, ABHYUDAYA NAGAR, KALACHOWKY, MUMBAI - 400033","city":"MUMBAI","district":"GREATER MUMBAI","state":"MAHARASHTRA"}]

> curl -H "Authorization: Bearer $access" https://deepsecurebank.herokuapp.com/fetchifsc/ifsc\=ABHY0065002/
[{"ifsc":"ABHY0065002","bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED","branch":"ABHYUDAYA NAGAR","address":"ABHYUDAYA EDUCATION SOCIETY, OPP. BLDG. NO. 18, ABHYUDAYA NAGAR, KALACHOWKY, MUMBAI - 400033","city":"MUMBAI","district":"GREATER MUMBAI","state":"MAHARASHTRA"}]

> curl -H "Authorization: Bearer $access" https://deepsecurebank.herokuapp.com/fetchifsc/ifsc\=ABHY00650EE02/
[{"Message":"NOT FOUND"}]

> curl -H "Authorization: Bearer $access" https://deepsecurebank.herokuapp.com/fetchifsc/                    
[{"Message":"bank ifsc code is required"}]

```

**NOTE**: You will need `jq` to installed on command line, else you can copy access token from `echo $out`
