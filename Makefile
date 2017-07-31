init:
	pip install -r requirements.txt

test:
	nosetests tests

wheel:
	pip wheel .

clean:
	git clean -Xdf

dist-clean:
	git clean -xdf
