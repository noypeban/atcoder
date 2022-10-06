export PATH=$PATH:${PWD}/node_modules/.bin

echo "acc login"
acc login
echo "oj login"
oj login -u $username -p $password https://atcoder.jp

alias test='oj t -c "python3 main.py" -d ./tests/'
alias submit='acc submit main.py'