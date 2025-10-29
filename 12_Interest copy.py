pip install mermaid-py

mermaid_code = """
graph TD
    subgraph "Decision Point"
        direction LR
        A[College Student in Taichung]
    end

    subgraph "Path 1: Prioritize Part-Time Job"
        direction TB
        B(Work during college)
        B --> C[Small Hourly Wage<br>(NT$190/hr)]
        C --> D[Immediate, Limited Cash Flow<br>(NT$114,000/year)]
        B --> E[Lower Academic Performance<br>Higher Stress]
        E --> F[Missed Career Opportunities]
    end

    subgraph "Path 2: Prioritize Academics"
        direction TB
        G(Focus on studies & skills)
        G --> H[Better Grades & Internships]
        H --> I[Higher Starting Salary<br>(~NT$34,000/month)]
        I --> J[Strong Career Growth<br>Comprehensive Benefits]
        G --> K[Long-Term Financial Security]
    end

    A --> |Choice A| B
    A --> |Choice B| G

    D --> L[**Immediate Gratification**<br>Limited Long-Term Potential]
    F --> M[**High Opportunity Cost**]
    J --> N[**Delayed Gratification**<br>High Lifetime Earning Potential]
    K --> O[**Secure Financial Future**]
"""
