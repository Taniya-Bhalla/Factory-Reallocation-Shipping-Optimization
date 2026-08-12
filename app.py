import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Factory Reallocation & Shipping Optimization",
    page_icon="🏭",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color: #F4F7FC;
}

[data-testid="stSidebar"] {
    background-color: #FFFFFF;
}

.main-title {
    color: #163A6B;
    font-size: 34px;
    font-weight: 700;
    margin-bottom: 0px;
}
h1, h2, h3 {
    color: #163A6B;
}
.subtitle {
    color: #64748B;
    font-size: 16px;
    margin-top: 4px;
    margin-bottom: 25px;
}

div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 18px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

div[data-testid="stMetricLabel"] {
    color: #64748B;
    font-weight: 600;
}

div[data-testid="stMetricValue"] {
    color: #163A6B;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

file_path = os.path.join(os.path.dirname(__file__), "final_dataset.xlsx")
df = pd.read_excel(file_path)

st.markdown(
    '<div class="main-title">🏭 Factory Reallocation & Shipping Optimization</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Interactive Recommendation & Analytics Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown("---")

st.sidebar.title("🔍 Dashboard Filters")
st.sidebar.caption("Use the filters to explore the data")

# Factory
factory_options = ["All"] + sorted(
    df["Factory"].dropna().astype(str).unique().tolist()
)

selected_factory = st.sidebar.selectbox(
    "🏭 Factory",
    factory_options
)

region_options = ["All"] + sorted(
    df["Region"].dropna().astype(str).unique().tolist()
)

selected_region = st.sidebar.selectbox(
    "🌎 Region",
    region_options
)

division_options = ["All"] + sorted(
    df["Division"].dropna().astype(str).unique().tolist()
)

selected_division = st.sidebar.selectbox(
    "🏢 Division",
    division_options
)

recommendation_options = ["All"] + sorted(
    df["Recommendation Status"]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)

selected_recommendation = st.sidebar.selectbox(
    "🎯 Recommendation",
    recommendation_options
)

risk_options = ["All"] + sorted(
    df["Risk Level"].dropna().astype(str).unique().tolist()
)

selected_risk = st.sidebar.selectbox(
    "⚠️ Risk Level",
    risk_options
)

lead_category_options = ["All"] + sorted(
    df["Lead Time Category"]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)

selected_lead_category = st.sidebar.selectbox(
    "⏱️ Lead Time Category",
    lead_category_options
)

shipping_options = ["All"] + sorted(
    df["Shipping Speed"]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)

selected_shipping = st.sidebar.selectbox(
    "🚚 Shipping Speed",
    shipping_options
)

filtered_df = df.copy()

if selected_factory != "All":
    filtered_df = filtered_df[
        filtered_df["Factory"].astype(str) == selected_factory
    ]

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"].astype(str) == selected_region
    ]

if selected_division != "All":
    filtered_df = filtered_df[
        filtered_df["Division"].astype(str) == selected_division
    ]

if selected_recommendation != "All":
    filtered_df = filtered_df[
        filtered_df["Recommendation Status"].astype(str)
        == selected_recommendation
    ]

if selected_risk != "All":
    filtered_df = filtered_df[
        filtered_df["Risk Level"].astype(str) == selected_risk
    ]

if selected_lead_category != "All":
    filtered_df = filtered_df[
        filtered_df["Lead Time Category"].astype(str)
        == selected_lead_category
    ]

if selected_shipping != "All":
    filtered_df = filtered_df[
        filtered_df["Shipping Speed"].astype(str)
        == selected_shipping
    ]

st.subheader("📊 Key Performance Indicators")

total_orders = len(filtered_df)

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Gross Profit"].sum()

total_units = filtered_df["Units"].sum()

avg_lead_time = filtered_df["Lead Time (Days)"].mean()

profit_margin = (
    (total_profit / total_sales) * 100
    if total_sales != 0
    else 0
)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric("📦 Total Orders", f"{total_orders:,}")

with col2:
    st.metric("💰 Total Sales", f"${total_sales:,.0f}")

with col3:
    st.metric("📈 Gross Profit", f"${total_profit:,.0f}")

with col4:
    st.metric("📦 Total Units", f"{total_units:,}")

with col5:
    st.metric("⏱️ Avg Lead Time", f"{avg_lead_time:.1f} days")

with col6:
    st.metric("💹 Profit Margin", f"{profit_margin:.1f}%")

highlight1, highlight2, highlight3 = st.columns(3)

top_sales_factory = (
    filtered_df.groupby("Factory")["Sales"]
    .sum()
    .idxmax()
)

top_sales_value = (
    filtered_df.groupby("Factory")["Sales"]
    .sum()
    .max()
)

top_recommended_factory = (
    filtered_df["Suggested Factory"]
    .value_counts()
    .idxmax()
)

top_recommended_orders = (
    filtered_df["Suggested Factory"]
    .value_counts()
    .max()
)

top_profit_factory = (
    filtered_df.groupby("Suggested Factory")["Expected Profit"]
    .sum()
    .idxmax()
)

top_profit_value = (
    filtered_df.groupby("Suggested Factory")["Expected Profit"]
    .sum()
    .max()
)

with highlight1:
    st.info(
        f"🏆 **Top Factory by Sales**\n\n"
        f"### {top_sales_factory}\n"
        f"Sales: **${top_sales_value:,.0f}**"
    )

with highlight2:
    st.info(
        f"🎯 **Most Recommended Factory**\n\n"
        f"### {top_recommended_factory}\n"
        f"Recommended Orders: **{top_recommended_orders:,}**"
    )

with highlight3:
    st.info(
        f"💰 **Highest Expected Profit**\n\n"
        f"### {top_profit_factory}\n"
        f"Expected Profit: **${top_profit_value:,.0f}**"
    )

st.markdown("---")

st.markdown(
    '<div class="section-title">💡 Key Insights</div>',
    unsafe_allow_html=True
)

top_factory = (
    filtered_df.groupby("Factory")["Sales"]
    .sum()
    .idxmax()
)

top_factory_sales = (
    filtered_df.groupby("Factory")["Sales"]
    .sum()
    .max()
)

reallocation_orders = (
    filtered_df["Recommendation Status"]
    .astype(str)
    .str.lower()
    .eq("reallocate")
    .sum()
)

avg_lead = filtered_df["Lead Time (Days)"].mean()

insight1, insight2, insight3 = st.columns(3)

with insight1:
    st.markdown(
        f"""
        <div class="footer-box">
        🏆 <b>Sales Leader</b><br><br>
        <span style="font-size:20px;color:#163A6B;">
        {top_factory}
        </span><br>
        <span style="color:#64748B;">
        Highest sales: ${top_factory_sales:,.0f}
        </span>
        </div>
        """,
        unsafe_allow_html=True
    )

with insight2:
    st.markdown(
        f"""
        <div class="footer-box">
        🎯 <b>Reallocation Opportunity</b><br><br>
        <span style="font-size:20px;color:#163A6B;">
        {reallocation_orders:,} orders
        </span><br>
        <span style="color:#64748B;">
        Recommended for reallocation
        </span>
        </div>
        """,
        unsafe_allow_html=True
    )

with insight3:
    st.markdown(
        f"""
        <div class="footer-box">
        ⏱️ <b>Average Lead Time</b><br><br>
        <span style="font-size:20px;color:#163A6B;">
        {avg_lead:.1f} days
        </span><br>
        <span style="color:#64748B;">
        Across filtered orders
        </span>
        </div>
        """,
        unsafe_allow_html=True
    )

col1, col2 = st.columns(2)

with col1:

    factory_sales = (
        filtered_df
        .groupby("Factory", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    fig_sales_factory = px.bar(
        factory_sales,
        x="Factory",
        y="Sales",
        title="💰 Sales by Factory",
        text_auto=".2s"
    )

    fig_sales_factory.update_layout(
        xaxis_title="Factory",
        yaxis_title="Sales"
    )

    st.plotly_chart(
        fig_sales_factory,
        use_container_width=True
    )

with col2:

    factory_profit = (
        filtered_df
        .groupby("Factory", as_index=False)["Gross Profit"]
        .sum()
        .sort_values("Gross Profit", ascending=False)
    )

    fig_profit_factory = px.bar(
        factory_profit,
        x="Factory",
        y="Gross Profit",
        title="📈 Gross Profit by Factory",
        text_auto=".2s"
    )

    fig_profit_factory.update_layout(
        xaxis_title="Factory",
        yaxis_title="Gross Profit"
    )

    st.plotly_chart(
        fig_profit_factory,
        use_container_width=True
    )

col1, col2 = st.columns(2)

with col1:

    region_sales = (
        filtered_df
        .groupby("Region", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    fig_region = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        title="🌎 Sales by Region",
        text_auto=".2s"
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

with col2:

    division_sales = (
        filtered_df
        .groupby("Division", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    fig_division = px.bar(
        division_sales,
        x="Division",
        y="Sales",
        title="🏢 Sales by Division",
        text_auto=".2s"
    )

    st.plotly_chart(
        fig_division,
        use_container_width=True
    )

col1, col2 = st.columns(2)

with col1:

    factory_orders = (
        filtered_df["Factory"]
        .value_counts()
        .reset_index()
    )

    factory_orders.columns = [
        "Factory",
        "Orders"
    ]

    fig_orders = px.bar(
        factory_orders,
        x="Factory",
        y="Orders",
        title="📦 Orders by Factory",
        text_auto=True
    )

    st.plotly_chart(
        fig_orders,
        use_container_width=True
    )

with col2:

    factory_units = (
        filtered_df
        .groupby("Factory", as_index=False)["Units"]
        .sum()
        .sort_values("Units", ascending=False)
    )

    fig_units = px.bar(
        factory_units,
        x="Factory",
        y="Units",
        title="📦 Units Sold by Factory",
        text_auto=".2s"
    )

    st.plotly_chart(
        fig_units,
        use_container_width=True
    )

st.markdown("---")

st.header("🎯 Factory Reallocation Recommendation")

st.caption(
    "Analysis of recommended factory allocation and associated risk levels."
)

recommendation_counts = (
    filtered_df["Recommendation Status"]
    .value_counts()
    .reset_index()
)

recommendation_counts.columns = [
    "Recommendation",
    "Count"
]

risk_counts = (
    filtered_df["Risk Level"]
    .value_counts()
    .reset_index()
)

risk_counts.columns = [
    "Risk Level",
    "Count"
]

col1, col2 = st.columns(2)

with col1:

    fig_recommendation = px.pie(
        recommendation_counts,
        names="Recommendation",
        values="Count",
        hole=0.55,
        title="Recommendation Status"
    )

    fig_recommendation.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig_recommendation.update_layout(
        height=400,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    st.plotly_chart(
        fig_recommendation,
        use_container_width=True
    )

with col2:

    fig_risk = px.pie(
        risk_counts,
        names="Risk Level",
        values="Count",
        hole=0.55,
        title="Risk Level Distribution"
    )

    fig_risk.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig_risk.update_layout(
        height=400,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    st.plotly_chart(
        fig_risk,
        use_container_width=True
    )

col1, col2 = st.columns(2)

with col1:

    lead_category = (
        filtered_df["Lead Time Category"]
        .value_counts()
        .reset_index()
    )

    lead_category.columns = [
        "Lead Time Category",
        "Count"
    ]

    fig_lead = px.bar(
        lead_category,
        x="Lead Time Category",
        y="Count",
        title="⏱️ Lead Time Category",
        text_auto=True
    )

    st.plotly_chart(
        fig_lead,
        use_container_width=True
    )

with col2:

    shipping_speed = (
        filtered_df["Shipping Speed"]
        .value_counts()
        .reset_index()
    )

    shipping_speed.columns = [
        "Shipping Speed",
        "Count"
    ]

    fig_shipping = px.bar(
        shipping_speed,
        x="Shipping Speed",
        y="Count",
        title="🚚 Shipping Speed",
        text_auto=True
    )

    st.plotly_chart(
        fig_shipping,
        use_container_width=True
    )

st.subheader("📅 Sales Trend")

monthly_sales = (
    filtered_df
    .groupby("Order Month", as_index=False)["Sales"]
    .sum()
)

fig_monthly = px.line(
    monthly_sales,
    x="Order Month",
    y="Sales",
    markers=True,
    title="📈 Monthly Sales Trend"
)

fig_monthly.update_layout(
    xaxis_title="Order Month",
    yaxis_title="Sales"
)

st.plotly_chart(
    fig_monthly,
    use_container_width=True
)

st.markdown("---")

st.header("🏭 Factory Recommendation & Expected Profit")

st.caption(
    "Recommended factory allocation and estimated profit impact."
)

col1, col2 = st.columns(2)

with col1:

    suggested_factory = (
        filtered_df["Suggested Factory"]
        .value_counts()
        .reset_index()
    )

    suggested_factory.columns = [
        "Suggested Factory",
        "Orders"
    ]

    fig_suggested = px.bar(
        suggested_factory,
        x="Suggested Factory",
        y="Orders",
        title="🏭 Suggested Factory by Orders",
        text_auto=True
    )

    fig_suggested.update_layout(
        height=420,
        xaxis_title="Suggested Factory",
        yaxis_title="Recommended Orders"
    )

    st.plotly_chart(
        fig_suggested,
        use_container_width=True
    )

st.markdown("---")

st.header("🔄 Current Factory vs Suggested Factory")

st.caption(
    "Order movement from the current factory to the recommended factory."
)

factory_movement = (
    filtered_df
    .groupby(
        ["Factory", "Suggested Factory"]
    )
    .size()
    .reset_index(name="Orders")
)

fig_movement = px.bar(
    factory_movement,
    x="Factory",
    y="Orders",
    color="Suggested Factory",
    barmode="group",
    title="Current Factory vs Suggested Factory",
    text_auto=True
)

fig_movement.update_layout(
    height=500,
    xaxis_title="Current Factory",
    yaxis_title="Number of Orders",
    legend_title="Suggested Factory"
)

st.plotly_chart(
    fig_movement,
    use_container_width=True
)

with col2:

    expected_profit = (
        filtered_df
        .groupby(
            "Suggested Factory",
            as_index=False
        )["Expected Profit"]
        .sum()
        .sort_values(
            "Expected Profit",
            ascending=False
        )
    )

    fig_expected = px.bar(
        expected_profit,
        x="Suggested Factory",
        y="Expected Profit",
        title="💰 Expected Profit by Suggested Factory",
        text_auto=".2s"
    )

    fig_expected.update_layout(
        height=420,
        xaxis_title="Suggested Factory",
        yaxis_title="Expected Profit"
    )

    st.plotly_chart(
        fig_expected,
        use_container_width=True
    )
    
st.markdown("---")

st.header("⏱️ Predicted Lead Time Analysis")

st.caption(
    "Model-predicted lead time across factories."
)

predicted_lead_time = (
    filtered_df
    .groupby("Suggested Factory", as_index=False)["Predicted Lead Time"]
    .mean()
    .sort_values("Predicted Lead Time")
)

fig_predicted_lead = px.bar(
    predicted_lead_time,
    x="Suggested Factory",
    y="Predicted Lead Time",
    title="Predicted Lead Time by Suggested Factory",
    text_auto=".1f"
)

fig_predicted_lead.update_layout(
    height=450,
    xaxis_title="Suggested Factory",
    yaxis_title="Predicted Lead Time"
)

st.plotly_chart(
    fig_predicted_lead,
    use_container_width=True
)

st.markdown("---")

with st.expander("📋 View Filtered Dataset"):

    st.caption(
        f"Showing {len(filtered_df):,} records after applying filters."
    )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=450
    )

st.markdown("---")

st.markdown(
    "<h3 style='text-align:center; color:#163A6B;'>"
    "🏭 Factory Reallocation & Shipping Optimization"
    "</h3>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:#64748B; font-size:16px;'>"
    "Interactive Recommendation & Analytics Dashboard"
    "</p>",
    unsafe_allow_html=True
)

info1, info2, info3 = st.columns(3)

with info1:
    st.markdown(
        """
        <div style="text-align:center;">
            <b>👩‍💻 Developed By</b><br>
            Taniya Bhalla
        </div>
        """,
        unsafe_allow_html=True
    )

with info2:
    st.markdown(
        """
        <div style="text-align:center;">
            <b>🎓 Department</b><br>
            Information Technology
        </div>
        """,
        unsafe_allow_html=True
    )

with info3:
    st.markdown(
        """
        <div style="text-align:center;">
            <b>🏫 University</b><br>
            Guru Jambheshwar University of Science & Technology
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("")

# Project objective
st.markdown(
    """
    <div style="
        background-color:#FFFFFF;
        padding:18px;
        border-radius:12px;
        border:1px solid #E2E8F0;
        text-align:center;
    ">
        <b style="color:#163A6B;">🎯 Project Objective</b><br><br>
        Optimize factory allocation by identifying suitable factories
        based on lead time, expected profit, shipping performance,
        risk level and recommendation status.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("")

st.markdown(
    "<p style='text-align:center; color:#163A6B; font-size:17px;'>"
    "<b>🛠️ Technologies Used</b>"
    "</p>",
    unsafe_allow_html=True
)

tool1, tool2, tool3, tool4, tool5, tool6 = st.columns(6)

with tool1:
    st.image(
        "https://cdn.simpleicons.org/python",
        width=45
    )
    st.caption("Python")

with tool2:
    st.image(
        "https://cdn.simpleicons.org/streamlit",
        width=45
    )
    st.caption("Streamlit")

with tool3:
    st.image(
        "https://cdn.simpleicons.org/pandas",
        width=45
    )
    st.caption("Pandas")

with tool4:
    st.image(
        "https://cdn.simpleicons.org/plotly",
        width=45
    )
    st.caption("Plotly")

with tool5:
    st.image(
        "https://img.icons8.com/color/96/microsoft-excel-2019.png",
        width=45
    )
    st.caption("Excel")
    
with tool6:
    st.image(
        "https://cdn.simpleicons.org/scikitlearn",
        width=45
    )
    st.caption("Scikit-learn")

st.markdown("")

st.markdown(
    "<p style='text-align:center; color:#94A3B8; font-size:13px;'>"
    "Data Analytics • Machine Learning • Recommendation System"
    "</p>",
    unsafe_allow_html=True
)
    
