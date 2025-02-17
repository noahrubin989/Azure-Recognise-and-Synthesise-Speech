# Azure - Speech Enabled Apps

---

## Azure Setup
The following is a guide on how to set up the required resource(s) for creating speech enabled apps.

### Create Resource
First create the resource by searching for **Speech services**, then **Create**.
<img width="1591" alt="Screenshot 2025-02-18 at 9 41 39 AM" src="https://github.com/user-attachments/assets/5dd95c73-0646-4cd8-83a9-e3e5f40a912b" />

Then, configure your resource to exist in a **Region** of your choice, using a **Pricing tier** set to **Free F0**. Once done, select **Review + Create**.

<img width="666" alt="Screenshot 2025-02-18 at 9 44 14 AM" src="https://github.com/user-attachments/assets/3b8a49a8-bd25-4017-8161-28e5e0c27e98" />

Then select **Create**. This will begin the deployment process of the resource to the resource group.

<img width="566" alt="Screenshot 2025-02-18 at 9 47 43 AM" src="https://github.com/user-attachments/assets/2eac0a1f-c04e-4a37-ab44-e89b289f47b1" />

### Explore resource
Navigate to the newly deployed resource. We will need the **Keys and endpoint** section for later when using the SDK.

<img width="1250" alt="Screenshot 2025-02-18 at 9 56 14 AM" src="https://github.com/user-attachments/assets/1364789e-f4c1-4a09-a5d0-995d7171dac4" />

---

## Code Steup

Create and activate new virtual environment for the project to install the correct libraries seamlessly.

```bash
python3 -m venv speech_env
```
```bash
source speech_env/bin/activate
```
