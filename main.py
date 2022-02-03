# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Transition:
    """A change from one state to a next"""

    def __init__(self, current_state, state_input, next_state):
        self.current_state = current_state
        self.state_input = state_input
        self.next_state = next_state

    def match(self, current_state, state_input):
        """Determines if the state and the input satisfies this transition relation"""
        return self.current_state == current_state and self.state_input == state_input

class FSM:
    """A basic model of computation"""

    def __init__(
            self,
            states=[],
            alphabet=[],
            accepting_states=[],
            initial_state=''):
        self.states = states
        self.alphabet = alphabet
        self.accepting_states = accepting_states
        self.initial_state = initial_state
        self.valid_transitions = False

    def add_transitions(self, transitions=[]):
        """Before we use a list of transitions, verify they only apply to our states"""
        for transition in transitions:
            if transition.current_state not in self.states:
                print(
                    'Invalid transition. {} is not a valid state'.format(
                        transition.current_state))
                return
            if transition.next_state not in self.states:
                print('Invalid transition. {} is not a valid state'.format)
                return
        self.transitions = transitions
        self.valid_transitions = True

    def __accept(self, current_state, state_input):
        """Looks to see if the input for the given state matches a transition rule"""
        # If the input is valid in our alphabet
        if state_input in self.alphabet:
            for rule in self.transitions:
                if rule.match(current_state, state_input):
                    return rule.next_state
            print('No transition for state and input')
            return None
        return None

    def accepts(self, sequence):
        """Process an input stream to determine if the FSM will accept it"""
        # Check if we have transitions
        if not self.valid_transitions:
            print('Cannot process sequence without valid transitions')

        print('Starting at {}'.format(self.initial_state))
        # When an empty sequence provided, we simply check if the initial state
        # is an accepted one
        if len(sequence) == 0:
            return self.initial_state in self.accepting_states

        # Let's process the initial state
        current_state = self.__accept(self.initial_state, sequence[0])
        if current_state is None:
            return False

        # Continue with the rest of the sequence
        for state_input in sequence[1:]:
            print('Current state is {}'.format(current_state))
            current_state = self.__accept(current_state, state_input)
            if current_state is None:
                return False

        print('Ending state is {}'.format(current_state))
        # Check if the state we've transitioned to is an accepting state
        return current_state in self.accepting_states



def main():
    # Set up our FSM with the required info:
    # Set of states
    states = ['State 1', 'State 2', 'Error']
    states = ['Idle', 'Wander', 'Talk', 'Barter', 'Ranged Attack', 'Melee Attack', 'Healing', 'Dead']
    # Set of allowed inputs
    alphabet = ['Idle chit-chat', 'Done talking', 'Walk', 'Stop', 'Talking', 'Trade', 'Done trade', '0HP',
                'Aggro close', 'Aggro far', 'Target lost', 'Target close', 'Target far', 'Low HP', 'High HP',
                'Told the funniest joke in the world', 'Informed about inflation']
    # Set of accepted states
    accepting_states = ['Dead']
    # The initial state
    initial_state = 'Idle'
    fsm = FSM(states, alphabet, accepting_states, initial_state)

    # Create the set of transitions
    transition1 = Transition('Idle', 'Idle chit-chat', 'Talk')
    transition2 = Transition('Idle', 'Walk', 'Wander')
    transition3 = Transition('Idle', '0HP', 'Dead')
    transition4 = Transition('Idle', 'Aggro close', 'Melee Attack')
    transition5 = Transition('Idle', 'Aggro far', 'Ranged Attack')
    transition6 = Transition('Wander', 'Stop', 'Idle')
    transition7 = Transition('Wander', 'Talking', 'Talk')
    transition8 = Transition('Wander', '0HP', 'Dead')
    transition9 = Transition('Talk', 'Done talking', 'Idle')
    transition10 = Transition('Talk', 'Walk', 'Wander')
    transition11 = Transition('Talk', 'Trade', 'Barter')
    transition12 = Transition('Talk', 'Told the funniest joke in the world', 'Dead')
    transition13 = Transition('Barter', 'Done Trade', 'Talk')
    transition14 = Transition('Barter', 'Informed about inflation', 'Dead')
    transition15 = Transition('Melee Attack', 'Target far', 'Ranged Attack')
    transition16 = Transition('Melee Attack', 'Low HP', 'Healing')
    transition17 = Transition('Melee Attack', '0HP', 'Dead')
    transition18 = Transition('Ranged Attack', 'Target lost', 'Idle')
    transition19 = Transition('Ranged Attack', 'Target close', 'Melee Attack')
    transition20 = Transition('Ranged Attack', 'Low HP', 'Healing')
    transition21 = Transition('Ranged Attack', '0HP', 'Dead')
    transition22 = Transition('Healing', 'High HP', 'Melee Attack')
    transition23 = Transition('Healing', 'High HP', 'Ranged Attack')
    transition24 = Transition('Healing', '0HP', 'Dead')

    transitions = [
        transition1,
        transition2,
        transition3,
        transition4,
        transition5,
        transition6,
        transition7,
        transition8,
        transition9,
        transition10,
        transition11,
        transition12,
        transition13,
        transition14,
        transition15,
        transition16,
        transition17,
        transition18,
        transition19,
        transition20,
        transition21,
        transition22,
        transition23,
        transition24]

    # Verify and add them to the FSM
    fsm.add_transitions(transitions)

    # Now that our FSM is correctly set up, we can give it input to process
    # Let's transition the FSM to a green light
    example1 = fsm.accepts(['Idle chit-chat', 'Trade', 'Informed about inflation'])
    print(example1)
    example2 = fsm.accepts(['Aggro close', 'Target far', 'Target lost', '0HP'])
    print(example2)
    example3 = fsm.accepts(['Walk', 'Stop', 'Aggro far', 'Low HP', '0HP'])
    print(example3)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
