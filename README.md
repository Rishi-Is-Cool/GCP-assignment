# CDAC-SM VITA Assignment: Cloud Storage + Cloud Run + Pub/Sub

## 🎯 Objective
Set up a system where uploading a file to a Cloud Storage bucket automatically triggers a Cloud Run service, which extracts file metadata and publishes it to a Pub/Sub topic.

---

## 🧱 Components

- Cloud Storage
- Cloud Run (Python, No Docker)
- Pub/Sub Topic + Pull Subscription
- Eventarc (No Cloud Function)

---

## 🔁 Flow

1. Upload file → Cloud Storage
2. Trigger → Eventarc
3. Handler → Cloud Run
4. Message → Pub/Sub

---

## 🔧 Steps Performed

- ✅ Created bucket: `cdac-vita-bucket`
- ✅ Created topic: `file-info-topic`
- ✅ Created subscription: `file-info-sub`
- ✅ Deployed Cloud Run from source (Python Flask)
- ✅ Connected bucket → Cloud Run via Eventarc
- ✅ Uploaded 7 files to bucket
- ✅ Captured logs from Cloud Run (7 screenshots)
- ✅ Pulled messages from Pub/Sub (1 screenshot)

---

## 📝 Example Log Output



