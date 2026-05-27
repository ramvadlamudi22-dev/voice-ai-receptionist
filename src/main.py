from pathlib import Path
import json


def load_sample_intake():
    path = Path(__file__).resolve().parent.parent / "sample" / "intake_form.json"
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_owner_summary(intake):
    return {
        "customer": intake.get("customer_name"),
        "request_type": intake.get("request_type"),
        "preferred_time": f"{intake.get('preferred_date')} {intake.get('preferred_time')}",
        "status": intake.get("status"),
        "summary": intake.get("summary"),
    }


def main():
    intake = load_sample_intake()
    summary = build_owner_summary(intake)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
