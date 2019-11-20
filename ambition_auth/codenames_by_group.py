from edc_auth import (
    AUDITOR,
    CLINIC,
    SCREENING,
    UNBLINDING_REQUESTORS,
    UNBLINDING_REVIEWERS,
    codenames_by_group,
)

from .codenames import (
    auditor,
    clinic,
    screening,
)

unblinding_requestors = []
unblinding_reviewers = []
codenames_by_group[AUDITOR] = auditor
codenames_by_group[CLINIC] = clinic
codenames_by_group[SCREENING] = screening
codenames_by_group[UNBLINDING_REQUESTORS] = unblinding_requestors
codenames_by_group[UNBLINDING_REVIEWERS] = unblinding_reviewers
