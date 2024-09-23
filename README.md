# Setup
This will download Lab 2 locally, allowing you to work on your scripts and upload (push) them back up to GitHub.

1. Use the Green "Code" button at the top of this page to copy the SSH link.
1. Clone your lab repository into your ~/ops445/lab2 directory:
```bash
git clone <ssh link> ~/ops445/lab2/
```
# Submission
1. Run the checking script:
```bash
cd ~/ops445/lab2/
pwd #confirm that you are in the right directory
python3 ./CheckLab2.py -f -v

Redirect the output of CheckLab2.py:
python3 ./CheckLab2.py -f -v &> laboutput.txt
```
Before moving on to the next step, make sure you identify any and all errors in your scripts.

In addition to the files you started with, your repository should contain the
following files you have created:

- [ ] lab2a.py
- [ ] lab2b.py
- [ ] lab2c.py
- [ ] lab2d.py
- [ ] lab2e.py
- [ ] lab2f.py
- [ ] lab2g.py
- [ ] laboutput.txt

2. Commit and push (upload) your Python scripts:
```bash
git add lab*
git commit -m "Individual message or note."
git push
```

You can make changes to your scripts and reupload as many times as you like. Make sure you commit+push to do so.

**Note:** Your lab is automatically submitted at the due date and time using the last published code. Any changes you publish after the due date won't be marked or seen by your professor.
