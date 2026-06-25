class ApprovalWorkflow:
    def __init__(self, approvers, thresholds):
        """
        Initialize a new workflow.
        :param approvers: List of approvers.
        :param thresholds: Definition of automatic rejection/escalation thresholds.
        """
        self.approvers = approvers
        self.thresholds = thresholds
        self.audit_trail = []

    def notify_approvers(self, request):
        """
        Notify all approvers about a new sensitive modification request.
        :param request: The request details.
        """
        for approver in self.approvers:
            print(f"Notifying {approver} by email and dashboard.")
        return "Notifications sent."

    def process_threshold(self, approval_count):
        """
        Handle thresholds.
        :param approval_count: Number of current approvals.
        """
        if approval_count >= self.thresholds['escalation']:
            return "Request escalated."
        elif approval_count <= self.thresholds['rejection']:
            return "Request rejected."
        return "Request pending approval."

    def log_decision(self, approver, decision):
        """
        Log any approval/rejection decisions.
        :param approver: Approver making the decision.
        :param decision: Decision made.
        """
        self.audit_trail.append((approver, decision))
        print(f"Logged: {approver} => {decision}")

# Example Usage
if __name__ == "__main__":
    workflow = ApprovalWorkflow(
        approvers=["manager1@example.com", "manager2@example.com"],
        thresholds={"rejection": 0, "escalation": 3},
    )
    workflow.notify_approvers("Modification Request #1234")
    print(workflow.process_threshold(1))
    workflow.log_decision("manager1@example.com", "Approved")