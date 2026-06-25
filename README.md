# Flask App Service Starter

A clean Flask starter with:

- Two routes: `/` and `/about`
- Responsive, modern UI (Jinja templates + custom CSS)
- Azure App Service deployment readiness

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── runtime.txt
├── startup.sh
├── templates/
│   ├── base.html
│   ├── index.html
│   └── about.html
└── static/
	 └── css/
		  └── styles.css
```

## Run Locally

1. Create and activate a virtual environment:

	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```

2. Install dependencies:

	```bash
	pip install -r requirements.txt
	```

3. Start the app:

	```bash
	python app.py
	```

4. Open:

	```text
	http://127.0.0.1:8000
	```

## Deploy To Azure App Service

### Option 1: Fastest (`az webapp up`)

1. Sign in and set subscription:

	```bash
	az login
	az account set --subscription "<YOUR_SUBSCRIPTION_NAME_OR_ID>"
	```

2. Deploy from this folder:

	```bash
	az webapp up \
	  --name <UNIQUE_APP_NAME> \
	  --resource-group <RESOURCE_GROUP_NAME> \
	  --runtime "PYTHON|3.11" \
	  --sku B1
	```

3. Configure startup command in App Service (if needed):

	```bash
	az webapp config set \
	  --resource-group <RESOURCE_GROUP_NAME> \
	  --name <UNIQUE_APP_NAME> \
	  --startup-file "./startup.sh"
	```

### Option 2: Azure Portal

1. Create a Linux App Service with Python 3.11.
2. Deploy this repository.
3. In Configuration > General settings, set Startup Command to:

	```text
	./startup.sh
	```

## Notes

- `requirements.txt` includes `gunicorn` for production hosting.
- `runtime.txt` pins Python version for platform compatibility.
- `startup.sh` binds to App Service `PORT` automatically.