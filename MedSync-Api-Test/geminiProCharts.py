import matplotlib.pyplot as plt

def plot_accuracy_trends(iterations, english_accuracies, formal_arabic_accuracies, colloquial_arabic_accuracies):
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, english_accuracies, marker='o', linestyle='-', color='#3E69FE', label='English')
    plt.plot(iterations, formal_arabic_accuracies, marker='s', linestyle='--', color='#69A1FD', label='Arabic')
    plt.plot(iterations, colloquial_arabic_accuracies, marker='^', linestyle='-.', color='#9BC4FD', label='Colloquial Arabic')

    plt.xlabel('Iterations')
    plt.ylabel('Accuracy (%)')
    plt.title('Model Accuracy Trends by Language')
    plt.grid(True)
    plt.legend()
    plt.ylim(0, 100)  # Set y-axis limit from 0 to 100%

    plt.show()

# Example usage: replace with your actual data
iterations = [1, 2, 3, 4, 5,6,7,8,9,10]
english_accuracies = [83, 84.3, 85.1, 83.8, 84.5,80, 80, 83.5, 83.333, 89.5]
formal_arabic_accuracies = [76.2, 77.5, 78.3, 76.9, 83.8,76.2, 77.5, 78.3, 76.9, 83.8]
colloquial_arabic_accuracies = [77.5, 80.1, 71.5, 60.3, 68.2,77.33, 72.5, 78.3, 76.9, 79.8]




def plot_accuracy_distribution(english_accuracy, formal_arabic_accuracy, colloquial_arabic_accuracy):
    languages = ['English', 'Arabic', 'Colloquial Arabic']
    accuracies = [english_accuracy, formal_arabic_accuracy, colloquial_arabic_accuracy]

    plt.figure(figsize=(8, 8))
    plt.pie(accuracies, labels=languages, autopct='%1.1f%%', colors=['#3E69FE', '#69A1FD', '#9BC4FD'], startangle=140)
    plt.title('Model Accuracy Distribution by Language')
    plt.show()

# Example usage: replace with your actual data
english_accuracy = 89.56
formal_arabic_accuracy = 78.80
colloquial_arabic_accuracy = 77.23




def plot_custom_color_bar(languages, accuracies):
    # Define colors for each bar
    colors = ['#3E69FE', '#FFA114', '#FF7F0E']  # Blue, Yellow, and a blend color

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot bars with custom colors
    bars = ax.bar(languages, accuracies, color=colors)

    # Add text annotations
    for bar, acc in zip(bars, accuracies):
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval, f'{acc:.1f}%', ha='center', va='bottom', fontsize=10)

    # Customize plot appearance
    ax.set_xlabel('Languages')
    ax.set_ylabel('Accuracy (%)')
    ax.set_title('Model Accuracy Comparison by Language')
    ax.set_ylim(0, 100)  # Set y-axis limit from 0 to 100%
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.show()


languages = ['English', 'Arabic', 'Colloquial Arabic']
accuracies = [89.5, 78.8, 77.2]  

plot_custom_color_bar(languages, accuracies)
plot_accuracy_trends(iterations, english_accuracies, formal_arabic_accuracies, colloquial_arabic_accuracies)
plot_accuracy_distribution(english_accuracy, formal_arabic_accuracy, colloquial_arabic_accuracy)
