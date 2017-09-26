function [makespan, assigns, accumulators] = greedy_balance(machine_num, job_num, job_indices, job_time)
% *********************************************************************** %
% Greedy Balance Algorithm for Loading Balancing Problem.
% --------
% INPUT  :
% --------
%   machine_num : matrix(1, 1), Integer
%   job_num     : matrix(1, 1), Integer
%   job_indices : matrix(1, job_num), Integer
%   job_time    : matrix(1, job_num), Double
%                 there is an one-to-one mapping relationship between \
%                   *job_indices* and *job_time*
% --------
% OUTPUT :
% --------
%   makespan    : matrix(1, 1), Double
%   assigns     : cell(1, machine_num), Integer
%                 all job indices on each machine [from bottom to top]
%   accumulators: matrix(1, machine_num), Integer
%                 total processing time on each machine
% --------
% Example:
% --------
%   >> [makespan, assigns, accumulators] = greedy_balance(3, 7, 1 : 7, 1 : 7); % 12
%   >> [makespan, assigns, accumulators] = greedy_balance(3, 6, 1 : 6, [2 3 4 6 2 2]); % 8
%   >> [makespan, assigns, accumulators] = greedy_balance(4, 13, [2 : 13 1], [ones(1, 12) 4]); % 7 <= 2 * 4 (4 = opt)
%   >> [makespan, assigns, accumulators] = greedy_balance(3, 5, 1 : 5, [7 6 5 4 2]); % 9
%       vs. [makespan, assigns, accumulators] = greedy_balance(3, 5, 1 : 5, [2 7 6 5 4]); % 10
%   >> job_time = randi(RandStream('mt19937ar', 'Seed', 0), 1e3, 1, 1e3); % job_time(1 , [1 end]) == [815   867]
%   >> [makespan, assigns, accumulators] = greedy_balance(100, 1e3, 1 : 1e3, job_time); % 5481
% *********************************************************************** %
    assigns = cell(1, machine_num);
    accumulators = zeros(1, machine_num);
    for job_ind = 1 : length(job_indices)
        [~, min_ind] = min(accumulators); % get the index of machine with a minimal load
        assigns{1, min_ind} = cat(2, assigns{1, min_ind}, job_indices(1, job_ind));
        accumulators(1, min_ind) = accumulators(1, min_ind) + job_time(1, job_ind);
    end
    makespan = max(accumulators);
end
