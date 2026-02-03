#!/usr/bin/env python3
"""
Close.io API Client
Wrapper for Close.io CRM API operations.

Environment Variables Required:
    CLOSE_API_KEY: Your Close.io API key

Usage:
    from close_io.client import CloseClient

    client = CloseClient()
    leads = client.get_leads(status="Qualified")
"""

import os
import json
import requests
from datetime import datetime
from typing import Dict, List, Optional, Any


class CloseClient:
    """Close.io API Client."""

    BASE_URL = "https://api.close.com/api/v1"

    def __init__(self, api_key: str = None):
        """Initialize with API key."""
        self.api_key = api_key or os.environ.get("CLOSE_API_KEY")
        if not self.api_key:
            raise ValueError("CLOSE_API_KEY required")

        self.session = requests.Session()
        self.session.auth = (self.api_key, "")
        self.session.headers.update({
            "Content-Type": "application/json"
        })

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict:
        """Make API request."""
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.request(method, url, **kwargs)

        if response.status_code >= 400:
            raise Exception(f"API Error {response.status_code}: {response.text}")

        return response.json() if response.text else {}

    # ==================== LEADS ====================

    def get_leads(
        self,
        status: str = None,
        query: str = None,
        limit: int = 100,
        skip: int = 0
    ) -> List[Dict]:
        """
        Get leads with optional filtering.

        Args:
            status: Filter by lead status name
            query: Close.io search query
            limit: Max results to return
            skip: Number to skip (pagination)

        Returns:
            List of lead dictionaries
        """
        params = {"_limit": limit, "_skip": skip}

        if query:
            params["query"] = query
        elif status:
            params["query"] = f'lead_status:"{status}"'

        result = self._request("GET", "lead", params=params)
        return result.get("data", [])

    def get_lead(self, lead_id: str) -> Dict:
        """Get single lead by ID."""
        return self._request("GET", f"lead/{lead_id}")

    def create_lead(self, data: Dict) -> Dict:
        """
        Create a new lead.

        Args:
            data: Lead data including:
                - name (required): Company/lead name
                - contacts: List of contact dicts
                - custom: Custom field values

        Returns:
            Created lead dictionary
        """
        return self._request("POST", "lead", json=data)

    def update_lead(self, lead_id: str, data: Dict) -> Dict:
        """Update existing lead."""
        return self._request("PUT", f"lead/{lead_id}", json=data)

    def update_lead_status(self, lead_id: str, status_id: str) -> Dict:
        """Update lead status."""
        return self.update_lead(lead_id, {"status_id": status_id})

    # ==================== LEAD STATUSES ====================

    def get_lead_statuses(self) -> List[Dict]:
        """Get all lead statuses."""
        result = self._request("GET", "status/lead")
        return result.get("data", [])

    def get_status_id(self, status_name: str) -> Optional[str]:
        """Get status ID by name."""
        statuses = self.get_lead_statuses()
        for status in statuses:
            if status["label"].lower() == status_name.lower():
                return status["id"]
        return None

    # ==================== CONTACTS ====================

    def get_contacts(self, lead_id: str) -> List[Dict]:
        """Get contacts for a lead."""
        result = self._request("GET", "contact", params={"lead_id": lead_id})
        return result.get("data", [])

    def create_contact(self, lead_id: str, data: Dict) -> Dict:
        """
        Create contact on a lead.

        Args:
            lead_id: Lead to add contact to
            data: Contact data including:
                - name (required)
                - emails: List of email dicts
                - phones: List of phone dicts
                - title: Job title
        """
        data["lead_id"] = lead_id
        return self._request("POST", "contact", json=data)

    # ==================== ACTIVITIES ====================

    def get_activities(
        self,
        lead_id: str = None,
        activity_type: str = None,
        limit: int = 50
    ) -> List[Dict]:
        """Get activities (calls, emails, notes)."""
        params = {"_limit": limit}

        if lead_id:
            params["lead_id"] = lead_id
        if activity_type:
            params["_type"] = activity_type

        result = self._request("GET", "activity", params=params)
        return result.get("data", [])

    def create_note(self, lead_id: str, note: str) -> Dict:
        """Create a note on a lead."""
        data = {
            "lead_id": lead_id,
            "note": note
        }
        return self._request("POST", "activity/note", json=data)

    def log_call(
        self,
        lead_id: str,
        direction: str,
        duration: int,
        note: str = ""
    ) -> Dict:
        """
        Log a call activity.

        Args:
            lead_id: Lead ID
            direction: "inbound" or "outbound"
            duration: Duration in seconds
            note: Call notes
        """
        data = {
            "lead_id": lead_id,
            "direction": direction,
            "duration": duration,
            "note": note
        }
        return self._request("POST", "activity/call", json=data)

    # ==================== TASKS ====================

    def get_tasks(
        self,
        is_complete: bool = False,
        assigned_to: str = None,
        due_date: str = None
    ) -> List[Dict]:
        """Get tasks (follow-ups)."""
        params = {"is_complete": is_complete}

        if assigned_to:
            params["assigned_to"] = assigned_to
        if due_date:
            params["due_date"] = due_date

        result = self._request("GET", "task", params=params)
        return result.get("data", [])

    def create_task(
        self,
        lead_id: str,
        text: str,
        due_date: str,
        assigned_to: str = None
    ) -> Dict:
        """Create a task/follow-up."""
        data = {
            "lead_id": lead_id,
            "text": text,
            "due_date": due_date,
            "is_complete": False
        }
        if assigned_to:
            data["assigned_to"] = assigned_to

        return self._request("POST", "task", json=data)

    def complete_task(self, task_id: str) -> Dict:
        """Mark task as complete."""
        return self._request("PUT", f"task/{task_id}", json={"is_complete": True})

    # ==================== OPPORTUNITIES ====================

    def get_opportunities(self, lead_id: str = None) -> List[Dict]:
        """Get opportunities (deals)."""
        params = {}
        if lead_id:
            params["lead_id"] = lead_id

        result = self._request("GET", "opportunity", params=params)
        return result.get("data", [])

    def create_opportunity(
        self,
        lead_id: str,
        value: int,
        value_period: str = "one_time",
        status_id: str = None,
        note: str = ""
    ) -> Dict:
        """
        Create an opportunity.

        Args:
            lead_id: Lead ID
            value: Deal value in cents
            value_period: "one_time", "monthly", "annual"
            status_id: Opportunity status ID
            note: Notes
        """
        data = {
            "lead_id": lead_id,
            "value": value,
            "value_period": value_period,
            "note": note
        }
        if status_id:
            data["status_id"] = status_id

        return self._request("POST", "opportunity", json=data)

    # ==================== CUSTOM FIELDS ====================

    def get_custom_fields(self) -> List[Dict]:
        """Get all custom field definitions."""
        result = self._request("GET", "custom_field/lead")
        return result.get("data", [])

    def set_custom_field(self, lead_id: str, field_name: str, value: Any) -> Dict:
        """
        Set a custom field value on a lead.

        Args:
            lead_id: Lead ID
            field_name: Custom field name (e.g., "custom.Lead Source")
            value: Value to set
        """
        # Get field ID if name provided
        if not field_name.startswith("custom."):
            field_name = f"custom.{field_name}"

        return self.update_lead(lead_id, {field_name: value})

    # ==================== SEARCH ====================

    def search(self, query: str, limit: int = 100) -> List[Dict]:
        """
        Search leads using Close.io query syntax.

        Examples:
            'lead_status:"Qualified"'
            'email_address:*@company.com'
            'custom."Lead Source":"Facebook"'
        """
        return self.get_leads(query=query, limit=limit)

    # ==================== SMART VIEWS ====================

    def get_smart_views(self) -> List[Dict]:
        """Get all smart views."""
        result = self._request("GET", "saved_search")
        return result.get("data", [])

    def get_smart_view_leads(self, view_id: str, limit: int = 100) -> List[Dict]:
        """Get leads from a smart view."""
        view = self._request("GET", f"saved_search/{view_id}")
        query = view.get("query", "")
        return self.search(query, limit)


# ==================== CONVENIENCE FUNCTIONS ====================

def get_today_tasks() -> List[Dict]:
    """Get all tasks due today."""
    client = CloseClient()
    today = datetime.now().strftime("%Y-%m-%d")
    return client.get_tasks(due_date=today)


def get_overdue_tasks() -> List[Dict]:
    """Get all overdue tasks."""
    client = CloseClient()
    tasks = client.get_tasks(is_complete=False)
    today = datetime.now().date()

    overdue = []
    for task in tasks:
        due_date = datetime.fromisoformat(task["due_date"].replace("Z", "+00:00")).date()
        if due_date < today:
            overdue.append(task)

    return overdue


def get_hot_leads(days_inactive: int = 3) -> List[Dict]:
    """Get qualified leads with recent activity."""
    client = CloseClient()
    return client.search(f'lead_status:"Qualified" sort:date_updated desc')


if __name__ == "__main__":
    # Quick test
    import sys

    if len(sys.argv) < 2:
        print("Usage: python client.py <command>")
        print("Commands: statuses, hot_leads, today_tasks, overdue")
        sys.exit(1)

    command = sys.argv[1]

    try:
        client = CloseClient()

        if command == "statuses":
            for status in client.get_lead_statuses():
                print(f"  {status['label']}: {status['id']}")

        elif command == "hot_leads":
            leads = get_hot_leads()
            for lead in leads[:10]:
                print(f"  {lead['display_name']}")

        elif command == "today_tasks":
            for task in get_today_tasks():
                print(f"  {task['text']}")

        elif command == "overdue":
            for task in get_overdue_tasks():
                print(f"  {task['text']} (due: {task['due_date']})")

        else:
            print(f"Unknown command: {command}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
