OUT := template.json

template:
	tox -e py36 -- python -m bulletsite.build $(OUT)
