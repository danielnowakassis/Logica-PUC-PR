from manimlib import *

class aula2(Scene):
    def construct(self):
        table = r"""
        \begin{table}[]
        \centering
        \begin{tabular}{|l|l|l|}\hline
        T & F & n(p v q) \\\hline
        &  &    \\\hline
        &  &   \\\hline
        &  &      \\\hline    
        &  &      \\\hline
        \end{tabular}
        \end{table}
        """
        tex_table = TexText(table)
        tex_table. move_to([-4.5,0,0])
        p = Tex("p")
        q = Tex("q")
        pq = Tex("p \\Rightarrow q", color = GREEN_SCREEN)
        p.move_to([-6.2,1.2,0])
        q.move_to([-5.2,1.2,0])
        pq.move_to([-3.7,1.2,0])
        self.play(Write(tex_table),  Write(p), Write(q), Write(pq), run_time = 3)
        self.wait(9)
        pqex1 = Tex("p \\Rightarrow p")
        pqex1.move_to([1,1,0])
        self.play(Write(pqex1))
        self.wait(13)
        pqex2 = Tex("p \\Rightarrow p \\equiv \\lnot (p \\land \\lnot p)")
        pqex2.move_to([1,1,0])
        self.play(ReplacementTransform(pqex1,pqex2))
        self.wait(16)
        pqex3 = Tex("p \\Rightarrow q \\equiv \\lnot (p \\land \\lnot q)")
        pqex3.move_to([1,1,0])
        self.play(ReplacementTransform(pqex2,pqex3))
        self.wait(9.5)
        pqex4 = Text("V → V ≡ ~(V ^ ~V)", t2c = {"V" : BLUE, "F": RED_E})
        pqex4.move_to([1,1,0])
        self.play(ReplacementTransform(pqex3, pqex4))
        self.wait(4)
        pqex5 = Text("V → V ≡ ~(V ^ F)", t2c = {"V" : BLUE, "F": RED_E})
        pqex5.move_to([1,1,0])
        self.play(ReplacementTransform(pqex4, pqex5))
        self.wait(2)
        pqex6 = Text("V → V ≡ ~(F)", t2c = {"V" : BLUE, "F": RED_E})
        pqex6.move_to([1,1,0])
        self.play(ReplacementTransform(pqex5, pqex6))
        self.wait(3)
        pqex7 = Text("V → V ≡ V", t2c = {"V" : BLUE, "F": RED_E})
        pqex7.move_to([1,1,0])
        self.play(ReplacementTransform(pqex6, pqex7))
        pv1 = Tex("V", color= BLUE)
        pv2 = Tex("V", color= BLUE)
        pf1 = Tex("F", color= RED)
        pf2 = Tex("F", color= RED)
        #
        pv1.move_to([-6.2,0.6,0])
        pv2.move_to([-6.2,0,0])
        pf1.move_to([-6.2,-0.6,0])
        pf2.move_to([-6.2,-1.2,0])
        #
        qv1 = Tex("V", color= BLUE)
        qf1 = Tex("F", color= RED)
        qv2 = Tex("V", color= BLUE)
        qf2 = Tex("F", color= RED)
        #
        qv1.move_to([-5.2,0.6,0])
        qf1.move_to([-5.2,0,0])
        qv2.move_to([-5.2,-0.6,0])
        qf2.move_to([-5.2,-1.2,0])
        #
        pqv1 = Tex("V", color= BLUE)
        pqf1 = Tex("F", color= RED)
        pqv2 = Tex("V", color= BLUE)
        pqv3 = Tex("V", color= BLUE)
        #
        pqv1.move_to([-3.7,0.6,0])
        pqf1.move_to([-3.7,0,0])
        pqv2.move_to([-3.7,-0.6,0])
        pqv3.move_to([-3.7,-1.2,0])

        self.play(Write(pv1), Write(qv1), Write(pqv1), run_time = 2)
        self.wait(3)
        pqex8 = Text("V → F ≡ ~(V ^ ~F)", t2c = {"V" : BLUE, "F": RED_E})
        pqex8.move_to([1,1,0])
        self.play(ReplacementTransform(pqex7, pqex8))
        self.wait(7)
        pqex9 = Text("V → F ≡ ~(V ^ V)", t2c = {"V" : BLUE, "F": RED_E})
        pqex9.move_to([1,1,0])
        self.play(ReplacementTransform(pqex8, pqex9))
        self.wait(4)
        pqex10 = Text("V → F ≡ ~(V)", t2c = {"V" : BLUE, "F": RED_E})
        pqex10.move_to([1,1,0])
        self.play(ReplacementTransform(pqex9, pqex10))
        pqex11 = Text("V → F ≡ F", t2c = {"V" : BLUE, "F": RED_E})
        pqex11.move_to([1,1,0])
        self.wait(1)
        self.play(Write(pv2), Write(qf1), Write(pqf1),ReplacementTransform(pqex10, pqex11))
        self.wait(5)
        pqex12 = Text("F → q ≡ ~(F ^ ~q)", t2c = {"V" : BLUE, "F": RED_E})
        pqex12.move_to([1,1,0])
        self.play(ReplacementTransform(pqex11, pqex12))
        self.wait(6)
        pqex13 = Text("F → q ≡ ~(F)", t2c = {"V" : BLUE, "F": RED_E})
        pqex13.move_to([1,1,0])
        self.play(ReplacementTransform(pqex12, pqex13))
        self.wait(6)
        self.play(Write(pf1),Write(qv2),Write(pqv2),Write(pf2),Write(qf2),Write(pqv3))
        self.wait(5)