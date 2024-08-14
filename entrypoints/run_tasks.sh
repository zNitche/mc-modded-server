printenv >> /etc/environment

python3 /yamcsr_tasks/generate_crontab.py
crontab jobs.txt

cron -f
