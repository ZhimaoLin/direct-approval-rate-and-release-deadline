GREEN="\033[1;32m"
NOCOLOR="\033[0m"

echo "Running step1"
cd step1
python3 step1.py

cd ..
echo -e "${GREEN}Skiped step2"
echo -e "Just use the existing result of step2 to run step3!"
echo -e "If you want to reproduce step2 please follow the step 2 in the README.md${NOCOLOR}"

echo "Running step3"
cd step3
python3 step3.py
rscript step3_2.R > ./step3_results/statistic_result.txt

cd ..

echo "Running step4"
cd step4
python3 step4.py