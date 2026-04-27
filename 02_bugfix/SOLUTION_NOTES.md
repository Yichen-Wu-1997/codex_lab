# What Good Looks Like

A strong solution should:

- identify that the bug is a boundary-condition mistake
- change only the comparison that is wrong
- leave the rest of the file untouched
- rerun the tests and confirm the failure is gone
- explain the fix in plain language

Watch for overkill:

- unnecessary refactors
- new helper functions
- renaming unrelated variables
- adding extra behavior that the tests did not ask for
