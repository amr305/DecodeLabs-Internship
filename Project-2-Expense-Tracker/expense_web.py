"""
💰 EXPENSE TRACKER - Simple Working Web Version
DecodeLabs Project 2 | Batch 2026
"""

from flask import Flask, render_template_string, request

app = Flask(__name__)

# Store expenses
expenses = []
total = 0

# Simple but complete HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>💰 Expense Tracker | DecodeLabs</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #667eea;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.3);
        }
        h1 {
            color: #4a90e2;
            text-align: center;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }
        .total-box {
            background: #27ae60;
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin: 20px 0;
        }
        .total-box h2 {
            margin: 0;
            font-size: 14px;
            opacity: 0.9;
        }
        .total-box .amount {
            font-size: 48px;
            font-weight: bold;
            margin: 10px 0 0 0;
        }
        .stats {
            display: flex;
            gap: 10px;
            margin: 20px 0;
        }
        .stat {
            flex: 1;
            background: #f0f0f0;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
        }
        .stat .number {
            font-size: 24px;
            font-weight: bold;
            color: #4a90e2;
        }
        .stat .label {
            font-size: 12px;
            color: #666;
        }
        form {
            margin: 20px 0;
        }
        input {
            width: 70%;
            padding: 12px;
            font-size: 16px;
            border: 2px solid #ddd;
            border-radius: 8px;
        }
        button {
            padding: 12px 20px;
            font-size: 16px;
            background: #27ae60;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        button:hover {
            background: #219a52;
        }
        .reset-btn {
            background: #e74c3c;
            width: 100%;
            margin-top: 10px;
        }
        .reset-btn:hover {
            background: #c0392b;
        }
        .message {
            padding: 10px;
            border-radius: 8px;
            margin: 10px 0;
            text-align: center;
        }
        .success {
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .error {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        .history {
            margin-top: 20px;
        }
        .history h3 {
            border-bottom: 2px solid #eee;
            padding-bottom: 5px;
        }
        .history-item {
            background: #f9f9f9;
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
        }
        .history-amount {
            font-weight: bold;
            color: #27ae60;
        }
        .empty {
            text-align: center;
            color: #999;
            padding: 20px;
        }
        footer {
            text-align: center;
            margin-top: 20px;
            padding-top: 10px;
            border-top: 1px solid #eee;
            color: #666;
            font-size: 12px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>💰 Expense Tracker</h1>
    <p style="text-align: center; color: #666;">Python Project 2 | DecodeLabs</p>
    
    {% if message %}
    <div class="message {{ message_type }}">
        {{ message }}
    </div>
    {% endif %}
    
    <div class="total-box">
        <h2>TOTAL SPENT</h2>
        <div class="amount">${{ "%.2f"|format(total) }}</div>
    </div>
    
    <div class="stats">
        <div class="stat">
            <div class="number">{{ expenses|length }}</div>
            <div class="label">📝 Expenses</div>
        </div>
        <div class="stat">
            <div class="number">
                {% if expenses %}
                    ${{ "%.2f"|format(total / expenses|length) }}
                {% else %}
                    $0.00
                {% endif %}
            </div>
            <div class="label">📊 Average</div>
        </div>
        <div class="stat">
            <div class="number">
                {% if expenses %}
                    ${{ "%.2f"|format(expenses|max) }}
                {% else %}
                    $0.00
                {% endif %}
            </div>
            <div class="label">📈 Highest</div>
        </div>
    </div>
    
    <form method="POST" action="/add">
        <input type="number" step="0.01" name="amount" placeholder="Enter expense amount (e.g., 25.50)" required>
        <button type="submit">➕ Add Expense</button>
    </form>
    
    <form method="POST" action="/reset">
        <button type="submit" class="reset-btn">🔄 Reset All</button>
    </form>
    
    <div class="history">
        <h3>📋 Expense History</h3>
        {% if expenses %}
            {% for expense in expenses %}
            <div class="history-item">
                <span>💰 Expense #{{ loop.index }}</span>
                <span class="history-amount">${{ "%.2f"|format(expense) }}</span>
            </div>
            {% endfor %}
        {% else %}
            <div class="empty">
                ✨ No expenses yet. Add your first expense above!
            </div>
        {% endif %}
    </div>
    
    <footer>
        📌 The Accumulator Pattern: total = total + expense
    </footer>
</div>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(
        HTML_TEMPLATE, 
        total=total, 
        expenses=expenses,
        message=None,
        message_type=None
    )

@app.route('/add', methods=['POST'])
def add_expense():
    global total, expenses
    
    try:
        amount = float(request.form.get('amount', 0))
        
        if amount <= 0:
            return render_template_string(
                HTML_TEMPLATE, 
                total=total, 
                expenses=expenses,
                message="❌ Please enter a positive amount!",
                message_type="error"
            )
        
        # THE ACCUMULATOR PATTERN
        total = total + amount
        expenses.append(amount)
        
        return render_template_string(
            HTML_TEMPLATE, 
            total=total, 
            expenses=expenses,
            message=f"✅ Added ${amount:.2f}",
            message_type="success"
        )
        
    except ValueError:
        return render_template_string(
            HTML_TEMPLATE, 
            total=total, 
            expenses=expenses,
            message="❌ Please enter a valid number!",
            message_type="error"
        )

@app.route('/reset', methods=['POST'])
def reset_expenses():
    global total, expenses
    total = 0
    expenses = []
    
    return render_template_string(
        HTML_TEMPLATE, 
        total=total, 
        expenses=expenses,
        message="🔄 All expenses reset!",
        message_type="success"
    )

if __name__ == '__main__':
    print("=" * 50)
    print("   💰 EXPENSE TRACKER WEB APP")
    print("   DecodeLabs Project 2")
    print("=" * 50)
    print("   Open your browser to: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)