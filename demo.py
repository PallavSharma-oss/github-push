a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
?";'..'KeyboardInterrupt
sdicnsd
git "
wuefhidcsmxc
-wqdoals
#!/usr/bin/env sh

echo "Running Python syntax check..."

FILES=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')

if [ -n "$FILES" ]; then
  python -m py_compile $FILES
  if [ $? -ne 0 ]; then
    echo "❌ Commit blocked: Python syntax error"
    exit 1
  fi
fi

echo "✅ Syntax OK"
exit 0S