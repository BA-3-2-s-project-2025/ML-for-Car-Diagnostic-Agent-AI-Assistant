# car_diagnostic_ai.py
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random

class CarDiagnosticAI:
    def __init__(self):
        self.problem_data = {
            'Battery/Starting': {
                'symptoms': ['wont start', 'not starting', 'clicking sound', 'battery dead', 'no power', 'engine wont turn over'],
                'solutions': [
                    'Replace battery and clean terminals',
                    'Check alternator and charging system',
                    'Replace starter motor',
                    'Inspect ignition switch and wiring'
                ],
                'how_to_fix': [
                    'Step 1: Check battery voltage with multimeter (should be 12.6V+)',
                    'Step 2: Clean battery terminals with wire brush',
                    'Step 3: Test alternator output while engine running',
                    'Step 4: Check starter motor connections and power',
                    'Step 5: Inspect ignition switch and key cylinder'
                ],
                'severity': 'Medium'
            },
            'Engine': {
                'symptoms': ['engine light', 'misfire', 'overheating', 'smoke', 'stalling', 'rough idle', 'knocking'],
                'solutions': [
                    'Check engine codes with OBD2 scanner',
                    'Replace spark plugs and ignition coils',
                    'Check coolant levels and radiator',
                    'Inspect fuel system and filters'
                ],
                'how_to_fix': [
                    'Step 1: Use OBD2 scanner to read diagnostic trouble codes',
                    'Step 2: Check spark plugs for wear and proper gap',
                    'Step 3: Test ignition coils with multimeter',
                    'Step 4: Inspect coolant level and look for leaks',
                    'Step 5: Check fuel pressure and injector operation'
                ],
                'severity': 'High'
            },
            'Oil System': {
                'symptoms': ['oil leak', 'oil leaking', 'low oil', 'burning oil', 'oil light', 'oil puddle'],
                'solutions': [
                    'Identify and fix oil leak source',
                    'Replace oil pan gasket or valve cover gasket',
                    'Top up engine oil to proper level',
                    'Check for worn seals and gaskets'
                ],
                'how_to_fix': [
                    'Step 1: Locate oil leak source by cleaning engine and tracing fresh oil',
                    'Step 2: Check oil level and add oil if low',
                    'Step 3: Inspect common leak points: valve covers, oil pan, front/rear seals',
                    'Step 4: Replace leaking gaskets and seals',
                    'Step 5: Perform oil change with new filter'
                ],
                'severity': 'High'
            },
            'Brakes': {
                'symptoms': ['brake noise', 'squealing brakes', 'vibration when braking', 'soft brake pedal', 'brake warning'],
                'solutions': [
                    'Replace brake pads and rotors',
                    'Check brake fluid level and quality',
                    'Inspect brake calipers and lines',
                    'Bleed brake system if needed'
                ],
                'how_to_fix': [
                    'Step 1: Inspect brake pads for wear (replace if under 3mm)',
                    'Step 2: Check brake rotors for warping or scoring',
                    'Step 3: Test brake fluid quality and level',
                    'Step 4: Inspect brake calipers for proper operation',
                    'Step 5: Bleed brake system to remove air bubbles'
                ],
                'severity': 'High'
            },
            'Electrical': {
                'symptoms': ['lights dim', 'electrical issues', 'power windows not working', 'radio not working', 'flickering lights'],
                'solutions': [
                    'Check battery and alternator output',
                    'Inspect fuses and relays',
                    'Check wiring connections',
                    'Test electrical components'
                ],
                'how_to_fix': [
                    'Step 1: Test battery voltage and alternator output',
                    'Step 2: Check all relevant fuses in fuse box',
                    'Step 3: Inspect wiring harness for damage or corrosion',
                    'Step 4: Test individual components (windows, lights, radio)',
                    'Step 5: Check ground connections throughout vehicle'
                ],
                'severity': 'Medium'
            },
            'Transmission': {
                'symptoms': ['gear problems', 'shifting hard', 'slipping gears', 'transmission noise', 'delayed shifting'],
                'solutions': [
                    'Check transmission fluid level and condition',
                    'Perform transmission service',
                    'Inspect transmission solenoids',
                    'Check for computer system errors'
                ],
                'how_to_fix': [
                    'Step 1: Check transmission fluid level and color (should be red, not brown)',
                    'Step 2: Inspect for transmission fluid leaks',
                    'Step 3: Perform transmission fluid and filter change',
                    'Step 4: Test transmission solenoids and sensors',
                    'Step 5: Scan for transmission control module codes'
                ],
                'severity': 'High'
            },
            'Cooling System': {
                'symptoms': ['overheating', 'coolant leak', 'temperature high', 'steam from engine', 'heater not working'],
                'solutions': [
                    'Check coolant level and condition',
                    'Inspect radiator and hoses',
                    'Test thermostat operation',
                    'Check water pump function'
                ],
                'how_to_fix': [
                    'Step 1: Check coolant level in reservoir and radiator',
                    'Step 2: Inspect for coolant leaks at hoses and connections',
                    'Step 3: Test radiator cap pressure rating',
                    'Step 4: Check thermostat operation and replace if stuck',
                    'Step 5: Inspect water pump for leaks and proper operation'
                ],
                'severity': 'High'
            }
        }
    
    def analyze_problems(self, user_message):
        """Simple and reliable problem analysis"""
        try:
            user_text = user_message.lower().strip()
            detected_problems = []
            
            # Check for each problem type
            for problem_type, data in self.problem_data.items():
                for symptom in data['symptoms']:
                    if symptom in user_text:
                        detected_problems.append({
                            'type': problem_type,
                            'symptom': symptom,
                            'solutions': data['solutions'],
                            'how_to_fix': data['how_to_fix'],
                            'severity': data['severity']
                        })
                        break  # Only need one match per problem type
            
            if not detected_problems:
                return self._handle_unknown_problem(user_text)
            
            return self._format_results(detected_problems, user_text)
            
        except Exception as e:
            return {'error': f'Analysis failed: {str(e)}'}
    
    def _handle_unknown_problem(self, user_text):
        """Handle cases where no specific problems are detected"""
        general_solutions = [
            'Check basic maintenance items: oil level, coolant, battery connections',
            'Scan for diagnostic trouble codes with OBD2 scanner',
            'Inspect visible components for damage or leaks',
            'Test drive to reproduce the issue and note specific symptoms'
        ]
        
        general_how_to_fix = [
            'Step 1: Perform visual inspection of engine bay and undercarriage',
            'Step 2: Check all fluid levels (oil, coolant, brake, transmission)',
            'Step 3: Use OBD2 scanner to check for stored trouble codes',
            'Step 4: Test drive vehicle to identify when problem occurs',
            'Step 5: Consult repair manual or professional mechanic for specific guidance'
        ]
        
        return {
            'problem_classification': 'General Diagnosis Needed',
            'problem_description': 'Unable to identify specific issues from description',
            'severity': 'Unknown',
            'diagnosis': 'Further investigation required',
            'solutions': ' | '.join(general_solutions),
            'how_to_fix': '\n'.join(general_how_to_fix),
            'solution_to_use': 'Seek professional mechanical assistance',
            'confidence': 0.3,
            'multiple_problems': False,
            'problem_count': 0
        }
    
    def _format_results(self, detected_problems, user_text):
        """Format the analysis results"""
        if len(detected_problems) == 1:
            return self._format_single_problem(detected_problems[0])
        else:
            return self._format_multiple_problems(detected_problems)
    
    def _format_single_problem(self, problem):
        """Format results for a single problem"""
        return {
            'problem_classification': problem['type'],
            'problem_description': f"Detected: {problem['symptom']}",
            'severity': problem['severity'],
            'diagnosis': f"Based on symptoms: {problem['symptom']}",
            'solutions': ' | '.join(problem['solutions']),
            'how_to_fix': '\n'.join(problem['how_to_fix']),
            'solution_to_use': random.choice(problem['solutions']),
            'confidence': 0.85,
            'multiple_problems': False,
            'problem_count': 1
        }
    
    def _format_multiple_problems(self, problems):
        """Format results for multiple problems"""
        problem_types = [p['type'] for p in problems]
        symptoms = [p['symptom'] for p in problems]
        all_solutions = []
        all_how_to_fix = []
        severities = [p['severity'] for p in problems]
        
        for problem in problems:
            all_solutions.extend(problem['solutions'][:2])  # Take top 2 solutions per problem
            all_how_to_fix.extend(problem['how_to_fix'][:3])  # Take top 3 steps per problem
        
        # Remove duplicates while preserving order
        unique_solutions = []
        for solution in all_solutions:
            if solution not in unique_solutions:
                unique_solutions.append(solution)
        
        unique_how_to_fix = []
        for step in all_how_to_fix:
            if step not in unique_how_to_fix:
                unique_how_to_fix.append(step)
        
        overall_severity = 'High' if 'High' in severities else 'Medium'
        
        return {
            'problem_classification': 'Multiple Issues',
            'problem_description': ' | '.join([f"{p['type']}: {p['symptom']}" for p in problems]),
            'severity': overall_severity,
            'diagnosis': f"Detected {len(problems)} issues: {', '.join(problem_types)}",
            'solutions': ' | '.join(unique_solutions),
            'how_to_fix': '\n'.join(unique_how_to_fix),
            'solution_to_use': 'Address issues in order of severity (High priority first)',
            'confidence': 0.75,
            'multiple_problems': True,
            'problem_count': len(problems)
        }

class ModernCarDiagnosticGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ML Car Diagnostic Agent AI Assistant")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2c3e50')
        
        # Initialize AI (no training needed)
        self.ai = CarDiagnosticAI()
        
        self.setup_gui()
    
    def setup_gui(self):
        # Main container
        main_container = tk.Frame(self.root, bg='#2c3e50')
        main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        header_frame = tk.Frame(main_container, bg='#2c3e50')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame, 
                              text="ML Car Diagnostic Agent AI Assistant",
                              font=('Arial', 20, 'bold'),
                              fg='white',
                              bg='#2c3e50')
        title_label.pack()
        
        subtitle_label = tk.Label(header_frame,
                                 text="Describe your car problems and get instant solutions",
                                 font=('Arial', 12),
                                 fg='#bdc3c7',
                                 bg='#2c3e50')
        subtitle_label.pack(pady=(5, 0))
        
        # Main content frame
        content_frame = tk.Frame(main_container, bg='#34495e')
        content_frame.pack(fill='both', expand=True)
        
        # Left side - Input
        left_frame = tk.Frame(content_frame, bg='white', relief='raised', bd=2)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        # Right side - Results
        right_frame = tk.Frame(content_frame, bg='white', relief='raised', bd=2)
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        self.setup_input_frame(left_frame)
        self.setup_results_frame(right_frame)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready - Describe your car problems above")
        status_bar = tk.Label(main_container, 
                             textvariable=self.status_var,
                             relief='sunken',
                             anchor='w',
                             bg='#34495e',
                             fg='white',
                             font=('Arial', 9))
        status_bar.pack(fill='x', pady=(10, 0))
    
    def setup_input_frame(self, parent):
        # Input header
        input_header = tk.Frame(parent, bg='#3498db', height=50)
        input_header.pack(fill='x')
        input_header.pack_propagate(False)
        
        input_title = tk.Label(input_header,
                              text="Describe Your Car Problems",
                              font=('Arial', 14, 'bold'),
                              fg='white',
                              bg='#3498db')
        input_title.pack(pady=15)
        
        # Input content
        input_content = tk.Frame(parent, bg='white', padx=20, pady=20)
        input_content.pack(fill='both', expand=True)
        
        # Problem description label
        desc_label = tk.Label(input_content,
                             text="What's wrong with your car?",
                             font=('Arial', 11, 'bold'),
                             fg='#2c3e50',
                             bg='white',
                             anchor='w')
        desc_label.pack(fill='x', pady=(0, 10))
        
        # Examples label
        examples_label = tk.Label(input_content,
                                text="Examples: 'car not starting' or 'engine overheating with oil leak'",
                                font=('Arial', 9),
                                fg='#7f8c8d',
                                bg='white',
                                anchor='w')
        examples_label.pack(fill='x', pady=(0, 5))
        
        # Problem input text area
        self.problem_text = scrolledtext.ScrolledText(input_content,
                                                     height=8,
                                                     width=50,
                                                     font=('Arial', 10),
                                                     relief='solid',
                                                     borderwidth=1,
                                                     padx=10,
                                                     pady=10)
        self.problem_text.pack(fill='both', expand=True)
        
        # Set placeholder text
        self.placeholder_text = "Example: My car won't start and I see oil leaking underneath..."
        self.problem_text.insert('1.0', self.placeholder_text)
        self.problem_text.config(fg='gray')
        self.problem_text.bind('<FocusIn>', self.clear_placeholder)
        self.problem_text.bind('<FocusOut>', self.restore_placeholder)
        self.placeholder_active = True
        
        # Analyze button
        analyze_btn = tk.Button(input_content,
                               text="ANALYZE CAR PROBLEMS",
                               font=('Arial', 12, 'bold'),
                               bg='#e74c3c',
                               fg='white',
                               relief='raised',
                               bd=0,
                               padx=20,
                               pady=10,
                               command=self.analyze_problems)
        analyze_btn.pack(pady=20)
        
        # Test buttons for quick examples
        test_frame = tk.Frame(input_content, bg='white')
        test_frame.pack(fill='x', pady=(10, 0))
        
        test_label = tk.Label(test_frame, text="Try examples:", font=('Arial', 9), bg='white', fg='#7f8c8d')
        test_label.pack(side='left')
        
        test_btn1 = tk.Button(test_frame, text="Won't start", font=('Arial', 8), 
                             command=lambda: self.set_example("My car won't start and makes clicking sounds"))
        test_btn1.pack(side='left', padx=5)
        
        test_btn2 = tk.Button(test_frame, text="Oil leak", font=('Arial', 8),
                             command=lambda: self.set_example("There's oil leaking from my car and the engine is overheating"))
        test_btn2.pack(side='left', padx=5)
        
        test_btn3 = tk.Button(test_frame, text="Brake noise", font=('Arial', 8),
                             command=lambda: self.set_example("My brakes are making squealing noises and the pedal feels soft"))
        test_btn3.pack(side='left', padx=5)
        
        test_btn4 = tk.Button(test_frame, text="Multiple issues", font=('Arial', 8),
                             command=lambda: self.set_example("Car won't start, oil is leaking, and brakes are noisy"))
        test_btn4.pack(side='left', padx=5)
    
    def set_example(self, example_text):
        """Set example text in the input field"""
        self.problem_text.delete('1.0', 'end')
        self.problem_text.insert('1.0', example_text)
        self.problem_text.config(fg='black')
        self.placeholder_active = False
    
    def clear_placeholder(self, event):
        """Clear placeholder text when user starts typing"""
        if self.placeholder_active:
            self.problem_text.delete('1.0', 'end')
            self.problem_text.config(fg='black')
            self.placeholder_active = False
    
    def restore_placeholder(self, event):
        """Restore placeholder text if nothing was entered"""
        if not self.problem_text.get('1.0', 'end-1c').strip():
            self.problem_text.insert('1.0', self.placeholder_text)
            self.problem_text.config(fg='gray')
            self.placeholder_active = True
    
    def setup_results_frame(self, parent):
        # Results header
        results_header = tk.Frame(parent, bg='#9b59b6', height=50)
        results_header.pack(fill='x')
        results_header.pack_propagate(False)
        
        results_title = tk.Label(results_header,
                                text="DIAGNOSIS RESULTS",
                                font=('Arial', 14, 'bold'),
                                fg='white',
                                bg='#9b59b6')
        results_title.pack(pady=15)
        
        # Results content
        results_content = tk.Frame(parent, bg='white', padx=20, pady=20)
        results_content.pack(fill='both', expand=True)
        
        # Results display area
        self.results_text = scrolledtext.ScrolledText(results_content,
                                                     height=20,
                                                     width=60,
                                                     font=('Arial', 10),
                                                     relief='solid',
                                                     borderwidth=1,
                                                     padx=10,
                                                     pady=10,
                                                     state='disabled')
        self.results_text.pack(fill='both', expand=True)
        
        # Initial placeholder text
        self.results_text.config(state='normal')
        self.results_text.insert('1.0', 
            "CAR DIAGNOSIS RESULTS\n\n"
            "Describe your car problems on the left\n"
            "and click 'ANALYZE CAR PROBLEMS' to get started.\n\n"
            "The AI will analyze your problems and provide:\n"
            "• Problem Classification\n"
            "• Symptoms Detected\n"
            "• Severity Level\n"
            "• Diagnosis\n"
            "• Recommended Solutions\n"
            "• HOW TO FIX - Step by Step Instructions\n\n"
            "Try the example buttons for quick testing!"
        )
        self.results_text.config(state='disabled')
    
    def analyze_problems(self):
        """Analyze the car problems - SIMPLIFIED AND RELIABLE"""
        user_input = self.problem_text.get('1.0', 'end-1c').strip()
        
        if not user_input or user_input == self.placeholder_text:
            messagebox.showwarning("Input Required", "Please describe your car problems first")
            return
        
        # Show immediate feedback
        self.status_var.set("Analyzing problems...")
        self.root.update()
        
        try:
            # Get analysis results
            result = self.ai.analyze_problems(user_input)
            
            if 'error' in result:
                messagebox.showerror("Analysis Error", result['error'])
                self.status_var.set("Analysis failed")
                return
            
            # Format and display results
            self.display_results(result)
            self.status_var.set(f"Analysis complete! Found {result.get('problem_count', 0)} problem(s)")
            
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {str(e)}")
            self.status_var.set("Analysis failed")
    
    def display_results(self, result):
        """Display the analysis results"""
        output = f"""
DIAGNOSIS RESULTS
{'='*50}

PROBLEM: {result['problem_classification']}

SYMPTOMS: {result['problem_description']}

SEVERITY: {result['severity']}

DIAGNOSIS: {result['diagnosis']}

RECOMMENDED SOLUTIONS: {result['solutions']}

{'='*50}
HOW TO FIX:
{'='*50}
{result['how_to_fix']}

{'='*50}
QUICK SOLUTION: {result['solution_to_use']}

CONFIDENCE: {result.get('confidence', 0.7)*100:.1f}%

{'='*50}
NOTE: For complex issues, consult a professional mechanic.
"""
        
        self.results_text.config(state='normal')
        self.results_text.delete('1.0', 'end')
        self.results_text.insert('1.0', output)
        self.results_text.config(state='disabled')

def main():
    try:
        root = tk.Tk()
        app = ModernCarDiagnosticGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"Error starting application: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    print("Starting Car Diagnostic AI Assistant...")
    print("No training required - ready to analyze problems!")
    main()
