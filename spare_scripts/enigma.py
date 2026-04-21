import itertools
import string

ALPHABET = string.ascii_uppercase

# ----------------------------
# GIVEN CONFIGURATION
# ----------------------------
ROTOR_WIRINGS = {
    "R1": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    "R2": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    "R3": "BDFHJLCPRTXVZNYEIWGAKMUSQO"
}

REFLECTOR = "LCBRWPZUMNXAIJQFODYVHTEKSG"

KNOWN_CIPHERTEXT = "MHNHBXLOOPPZLTUNMQQAZVEJTUMJLAULSLYPVKWEKYKEKFGNZFFAZPQFCSKHFGOODTKVZTHWURNOJKGQYVGBAGOQ"
KNOWN_PLAINTEXT  = "STARTTRANSMISSIONEXPERIENCINGTECHNICALDIFFICULTIESBUTWILLTRANSMITMESSAGEINFIFTEENMINUTES"

TARGET_CIPHERTEXT = "RMZHFXDZUDDWWZADXWOBFKXKTWRCEVRKCVSUTCJNHLYUXGEUCAUIBBJGVTEWSRWDFEPRUYPXTXPLAQGFCXJPTMZFEBJVBDIVSIVHCNHMKBGDWNOOQLYNAOTOHLPUZODL"

CRIB_LENGTH = 25  # early rejection window

# ----------------------------
# ROTOR CLASS
# ----------------------------
class Rotor:
    def __init__(self, wiring, position=0):
        self.wiring = wiring
        self.inverse = self._inverse_wiring(wiring)
        self.position = position

    def _inverse_wiring(self, wiring):
        inv = [''] * 26
        for i, c in enumerate(wiring):
            inv[ord(c) - 65] = chr(i + 65)
        return ''.join(inv)

    def forward(self, c):
        idx = (ord(c) - 65 + self.position) % 26
        out = self.wiring[idx]
        return chr((ord(out) - 65 - self.position) % 26 + 65)

    def backward(self, c):
        idx = (ord(c) - 65 + self.position) % 26
        out = self.inverse[idx]
        return chr((ord(out) - 65 - self.position) % 26 + 65)

    def step(self):
        self.position = (self.position + 1) % 26


# ----------------------------
# ENIGMA MACHINE
# ----------------------------
class Enigma:
    def __init__(self, rotors, reflector, positions, damage_model):
        self.rotors = [
            Rotor(rotors[i], positions[i]) for i in range(3)
        ]
        self.reflector = reflector
        self.damage_model = damage_model

    def step_rotors(self):
        if self.damage_model["type"] == "no_stepping":
            return

        if self.damage_model["type"] == "normal":
            # Only rightmost steps (simplified Enigma)
            self.rotors[2].step()
            return

        if self.damage_model["type"] == "stuck_1":
            stuck = self.damage_model["stuck"]
            for i in reversed(range(3)):
                if i == stuck:
                    continue
                self.rotors[i].step()
                break
            return

        if self.damage_model["type"] == "stuck_2":
            stuck_set = self.damage_model["stuck"]
            for i in reversed(range(3)):
                if i in stuck_set:
                    continue
                self.rotors[i].step()
                break
            return

    def encrypt_char(self, c):
        self.step_rotors()

        # forward
        for rotor in reversed(self.rotors):
            c = rotor.forward(c)

        # reflector
        c = self.reflector[ord(c) - 65]

        # backward
        for rotor in self.rotors:
            c = rotor.backward(c)

        return c

    def encrypt_partial_match(self, plaintext, ciphertext, length):
        """Early rejection comparison"""
        for i in range(length):
            c = self.encrypt_char(plaintext[i])
            if c != ciphertext[i]:
                return False
        return True

    def encrypt(self, text):
        result = ""
        for c in text:
            result += self.encrypt_char(c)
        return result


# ----------------------------
# DAMAGE MODELS
# ----------------------------
def generate_damage_models():
    models = []

    # Normal stepping
    models.append({"type": "normal"})

    # One rotor stuck
    for i in range(3):
        models.append({"type": "stuck_1", "stuck": i})

    # Two rotors stuck
    for combo in itertools.combinations([0,1,2], 2):
        models.append({"type": "stuck_2", "stuck": combo})

    # No stepping at all
    models.append({"type": "no_stepping"})

    return models


# ----------------------------
# BRUTE FORCE
# ----------------------------
def brute_force():
    rotor_names = ["R1", "R2", "R3"]
    rotor_permutations = list(itertools.permutations(rotor_names))
    damage_models = generate_damage_models()

    total = 0

    for perm in rotor_permutations:
        rotor_set = [ROTOR_WIRINGS[r] for r in perm]

        for damage_model in damage_models:
            for positions in itertools.product(range(26), repeat=3):

                total += 1
                if total % 50000 == 0:
                    print(f"Checked {total} configs...")

                machine = Enigma(
                    rotor_set,
                    REFLECTOR,
                    positions,
                    damage_model
                )

                # EARLY REJECTION HERE
                if not machine.encrypt_partial_match(
                    KNOWN_PLAINTEXT,
                    KNOWN_CIPHERTEXT,
                    CRIB_LENGTH
                ):
                    continue

                # FULL CHECK
                machine = Enigma(
                    rotor_set,
                    REFLECTOR,
                    positions,
                    damage_model
                )

                full = machine.encrypt(KNOWN_PLAINTEXT)

                if full == KNOWN_CIPHERTEXT:
                    print("\n=== FOUND MATCH ===")
                    print("Rotor Order:", perm)
                    print("Positions:", positions)
                    print("Damage Model:", damage_model)

                    return perm, positions, damage_model

    return None


# ----------------------------
# MAIN
# ----------------------------
def main():
    config = brute_force()

    if not config:
        print("No configuration found.")
        return

    perm, positions, damage_model = config

    rotor_set = [ROTOR_WIRINGS[r] for r in perm]

    machine = Enigma(
        rotor_set,
        REFLECTOR,
        positions,
        damage_model
    )

    decrypted = machine.encrypt(TARGET_CIPHERTEXT)

    print("\n=== DECRYPTED MESSAGE ===")
    print(decrypted)


if __name__ == "__main__":
    main()
