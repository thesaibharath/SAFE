# S.A.F.E: Sustainability Assessment Framework for the Environment 🌍

Welcome to **S.A.F.E (Sustainability Assessment Framework for the Environment)**, an interactive tool designed to help users assess their carbon emissions and provide insights to reduce their environmental impact.

**Developed by:** Sai Bharath & Suriyaa

## Key Features
- Calculate carbon emissions for Transportation, Electricity, Diet, and Waste.
- State-specific emission factors for Tamil Nadu, Delhi, Mumbai, and Puducherry.
- Detailed emissions breakdown and comparison with state/national averages.
- Visualization of historical CO₂ emission trends per capita.
- Personalized recommendations to lower your carbon footprint.
- Goal-setting for carbon footprint reduction.

## Prerequisites

- Python 3.7 or higher
- `streamlit`, `pandas`, `numpy`, `matplotlib`

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/<your-username>/SAFE.git
    ```
2. Navigate to the project directory:
    ```bash
    cd SAFE
    ```
3. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## How to Use S.A.F.E

1. **Account Creation**: 
   - On the first run, you'll be prompted to create an account with a username and password.
   - Your data will be saved locally.

2. **Carbon Emission Inputs**: 
   - **State Selection**: Choose your state (Tamil Nadu, Delhi, Mumbai, or Puducherry).
   - **Transportation**: Enter your mode of transport and daily travel distance.
   - **Electricity Consumption**: Provide your monthly electricity consumption.
   - **Waste Generation**: Enter the average weekly waste you generate.
   - **Diet**: Select your diet type and number of meals per day.

3. **Emissions Calculation**: 
   - Press the "Calculate" button to view your detailed carbon emissions breakdown.
   - Compare your emissions with the state average.

4. **Additional Features**: 
   - Historical emissions graph for CO₂ emissions per capita.
   - Recommendations to reduce your carbon footprint.
   - Set and track your carbon reduction goals.


## Visualization & Graphs

S.A.F.E provides interactive graphs to display historical CO₂ emissions for Tamil Nadu, Delhi, Mumbai, and Puducherry, allowing you to visualize changes over time. We utilize Matplotlib to create these informative plots.

## Contributing

We welcome contributions from the community! If you have ideas for new features, improvements, or bug fixes, please feel free to open an issue or create a pull request.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Commit and push your changes.
4. Submit a pull request for review.

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

## Contact

- **Developers**: Sai Bharath & Suriyaa
- For any questions or suggestions, please contact us at [bharathsai550@gmail.com](mailto: bharathsai550@gmail.com).

## Additional Resources

- [Basics of Climate Change](https://www.ipcc.ch/report/ar6/wg1/)
- [Carbon Footprint Calculator Guide](https://www.epa.gov/ghgemissions/calculating-carbon-footprint)